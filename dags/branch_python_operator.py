from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from datetime import datetime, timedelta

def _choose_best_model():
    accuracy = 6
    if accuracy > 5:
        return 'accurate'
    else:
        return 'inaccurate'
    
def _accurate():
    mention = 6
    if mention == 6:
        return 'mention'
    else:
        return 'mention_not'

def _inaccurate():
    print("inaccurate_dag_printed")

def _mention():
    print("mentioned")

def _mention_not():
    print("mention_not")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    # 'email_on_failure': False,
    # 'email_on_retry': False,
}

dag = DAG(
    dag_id = 'branch_python_operator_dag',
    default_args=default_args,
    description='A dag for branch_python_operator', 
    schedule_interval=timedelta(minutes=5),
    # schedule_interval='@once',
    catchup=False,
)

branching = BranchPythonOperator(
    task_id = "branch",
    python_callable = _choose_best_model,
    dag=dag
)

accurate = BranchPythonOperator(
    task_id = "accurate",
    python_callable = _accurate,
    dag=dag
)

inaccurate = PythonOperator(
    task_id = "inaccurate",
    python_callable = _inaccurate,
    dag=dag
)

mention = PythonOperator(
    task_id = "mention",
    python_callable = _mention,
    dag=dag
)

mention_not = PythonOperator(
    task_id = "mention_not",
    python_callable = _mention_not,
    dag=dag
)

branching >> [accurate, inaccurate]
accurate >> [mention, mention_not]