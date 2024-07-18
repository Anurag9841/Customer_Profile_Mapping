from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    # 'email_on_failure': False,
    # 'email_on_retry': False,
}
dag = DAG(
    'trigger_onrun_dag',
    default_args=default_args,
    description='A dag for branch_python_operator',
    schedule_interval='@once',
    catchup=False,
)

def downloading():
    print("downloading_complete")

def completion():
    print("completed_task")

trigger = TriggerDagRunOperator(
    task_id = "trigger",
    trigger_dag_id= "sql_sensor_dag",
    dag = dag
)
download = PythonOperator(
    task_id = "download",
    python_callable= downloading,
    dag = dag
)
completion = PythonOperator(
    task_id = "completion",
    python_callable=completion,
    dag = dag
)

download >> trigger >> completion