from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from hdfs import InsecureClient

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    # 'email_on_failure': False,
    # 'email_on_retry': False,
}
dag = DAG(
    'mysql_dump_dag',
    default_args=default_args,
    description='A dag for mysql_dump',
    schedule_interval='@once',
    catchup=False,
)

dump_command= """
mysqldump -u wsl_root -panurag123 -h 172.25.0.1 client_rw employee3 > /home/user/airflow/output_file/output_sql_dump/dumped_file1.sql
"""

# mysql_query = """
#     CREATE TABLE employee3(
#         name varchar(255)
#     );
# """

# mysql_task = MySqlOperator(
#     task_id='mysql_task',
#     mysql_conn_id='MySQLID',  # Connection ID as configured in Airflow
#     sql=mysql_query,
#     dag=dag,
# )

mysql_dump = BashOperator(
    task_id = 'mysql_dump',
    bash_command = dump_command,
    dag = dag
)

