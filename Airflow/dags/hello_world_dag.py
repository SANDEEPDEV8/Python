from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define a function to be executed by the PythonOperator
def print_hello():
    print("Hello World")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Instantiate the DAG
dag = DAG(
    'hello_world',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval='@daily',
)

# Define the tasks in the DAG
start = DummyOperator(
    task_id='start',
    dag=dag,
)

hello_world = PythonOperator(
    task_id='hello_world',
    python_callable=print_hello,
    dag=dag,
)

# Set the task dependencies
start >> hello_world
