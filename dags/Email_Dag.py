from airflow import DAG
from datetime import timedelta
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator



with DAG(
    dag_id='email_dag',
    schedule_interval="25 4 * * *",
    default_args={
        "owner":"airflow",
        "start_date":datetime(2024,4,27,3,50),
        # "retries":1,
        # "retry_delay":timedelta(minutes=1),
        "email":['anuragkarki34@outlook.com'],
        "email_on_failure":False,
        "email_on_retry":False,

    },
    catchup = False) as f:
    email = EmailOperator(
        task_id = 'send_email',
        to = ["anuragkarkikarki79@gmail.com","tseringnc707@gmail.com"],
        subject="Good Afternoon Message",
        html_content="""<h2>Good Afternoon-From Anurag Karki</h2>""",
    )
    email



