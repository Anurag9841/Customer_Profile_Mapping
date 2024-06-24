from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from utils.customer_map import mapping

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    'email_on_failure': False,
    'email_on_retry': False,
}
mydag = DAG(
    'customer_mapping',
    default_args=default_args,
    description='A dag for customer_mapping',
    schedule_interval='@once',
    catchup=False,
)
customer_mapping = PythonOperator(
    task_id = "customer_mapping",
    python_callable = mapping,
    dag = mydag,
)
customer_mapping