from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from utils.customer_profile import main

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    'email_on_failure': False,
    'email_on_retry': False,
}
dag = DAG(
    'customer_profile_creation_dag',
    default_args=default_args,
    description='A dag for customer_profile',
    schedule_interval='@once',
    catchup=False,
)
table_creation = PythonOperator(
    task_id = "table_creation",
    python_callable = main,
    dag = dag,
)
table_creation
