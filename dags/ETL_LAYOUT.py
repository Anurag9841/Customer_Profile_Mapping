# from airflow import DAG
# from airflow.operators.bash_operator import BashOperator
# from datetime import datetime, timedelta
# from airflow.operators.python_operator import PythonOperator

# from utils.etl_layouts import etl_layout

# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2024, 3, 14),
#     'email_on_failure': False,
#     'email_on_retry': False,
# }

# dag = DAG(
#     'ETL_LAYOUT_dag',
#     default_args=default_args,
#     description='A DAG for etl_layout_config',
#     schedule_interval='@once',
#     catchup=False,
# )

# etl_layout_= PythonOperator(
#     task_id = "output",
#     python_callable = etl_layout,
#     dag = dag
# )
# etl_layout_