from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
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
mysqldump -u wsl_root -ppassword -h 172.25.0.1 store_procedure products > /home/user/airflow/output_file/output_sql_dump/dumped_file.sql
"""

table_insertion = BashOperator(
    task_id='table_creation',
    bash_command=dump_command,
    dag=dag,
)