from airflow import DAG
from airflow.sensors.sql import SqlSensor
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    # 'email_on_failure': False,
    # 'email_on_retry': False,
}

dag = DAG(
    'sql_sensor_dag',
    default_args=default_args,
    description='A dag for branch_python_operator',
    schedule_interval='@once',
    catchup=False,
)

sqlsensor = SqlSensor(
    task_id = "sqlsensor",
    conn_id = "MySQLID",
    sql = "select * from client_rw.fc_account_master where active_flag = 1",
    mode = "poke",
    poke_interval = 20,
    timeout = 100,
    dag = dag
)
def waiting():
    print("data with active_flag 1 found")

waitings = PythonOperator(
    task_id = "waitings",
    python_callable = waiting,
    dag = dag
)

sqlsensor >> waitings