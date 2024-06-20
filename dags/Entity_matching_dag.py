from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

from utils.preprocess_combination import final_entity_matching

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'Entity_matching_dag',
    default_args=default_args,
    description='A DAG for entity matching',
    schedule_interval='@once',
    catchup=False,
)

final_df = PythonOperator(
    task_id = "output",
    python_callable = final_entity_matching,
    dag = dag
)
final_df





