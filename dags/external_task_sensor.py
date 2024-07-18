from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    # 'email_on_failure': False,
    # 'email_on_retry': False,
}

dag = DAG(
    'external_task_sensor_dag',
    default_args=default_args,
    description='A dag for external_task_sensor',
    schedule_interval=timedelta(minutes=5),
    catchup=False,
)
def second_task():
    print("Dependednt_Task executed")
    
externaltask = ExternalTaskSensor(
    task_id = "External_Task",
    external_dag_id = "branch_python_operator_dag",
    external_task_id = "branch",
    # execution_delta = timedelta(minutes=10),
    # mode = "poke",
    # timeout = 60,
    dag = dag
)
dependent_task = PythonOperator(
    task_id = "dependent_task",
    python_callable= second_task,
    dag = dag
)
externaltask >> dependent_task

