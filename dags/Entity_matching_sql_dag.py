'''
Author: Anurag Karki
Date: 2024/07/22
'''
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

from utils.preprocess_combination_sql import final_entity_matching
from utils.sql_file_dump import load_df_from_sql

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',  # The owner of the DAG
    'start_date': datetime(2024, 3, 14),  # Start date for scheduling the DAG
    'email_on_failure': False,  # Disable email notifications on task failure
    'email_on_retry': False,  # Disable email notifications on task retry
}

# Create the DAG instance
dag = DAG(
    'Entity_matching_dag_sql',  # Unique identifier for the DAG
    default_args=default_args,  # Default arguments for the DAG
    description='A DAG for entity matching',  # Description of the DAG
    schedule_interval='@once',  # Schedule the DAG to run only once
    catchup=False,  # Prevent backfilling of past dates
)

# Define a task that runs the load_df_from_sql function
load_file_sql = PythonOperator(
    task_id="input",
    python_callable=load_df_from_sql,
    dag=dag
)

# Define a task that runs the final_entity_matching function
final_df_sql = PythonOperator(
    task_id="output",  # Unique identifier for the task
    python_callable=final_entity_matching,  # The function to call when running this task
    dag=dag  # The DAG instance this task belongs to
)

# Define the task sequence
load_file_sql >> final_df_sql