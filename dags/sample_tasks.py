import datetime as dt

import airflow
from airflow import DAG

from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(20, 5, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

def print_world():
    print('world')


with DAG('airflow_tutorial_v01',
         default_args=default_args,
         schedule_interval=None,
         ) as dag:

    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)


print_world
