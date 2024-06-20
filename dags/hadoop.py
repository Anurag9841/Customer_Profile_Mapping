
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from hdfs import InsecureClient

def upload_to_hdfs():
    hdfs_client = InsecureClient('http://172.25.0.1:9870',user = 'acer')
    
    # Define local and HDFS file paths
    local_file_path = "dags/Email_Dag.py"
    hdfs_upload_path = '/anurag/Email_Dag.py'

    # Upload file from local to HDFS
    try:
        hdfs_client.upload(hdfs_upload_path, local_file_path)
        print("File uploaded to HDFS successfully!")
    except Exception as e:
        print(f"Error uploading file: {e}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    # 'email_on_failure': False,
    # 'email_on_retry': False,
}
dag = DAG(
    'hadoop_dag',
    default_args=default_args,
    description='A dag for customer_profile',
    schedule_interval='@once',
    catchup=False,
)
table_insertion = PythonOperator(
    task_id = "table_creation",
    python_callable = upload_to_hdfs,
    dag = dag,
)