from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from flask import stream_template

default_args = {
    'owner': 'indranil',
    'start_date': datetime(2028, 2, 28)
}

def stream_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/")
    print(res.json())

with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    streaming_task = PythonOperator(
    task_id='streaming_task_api',
    python_callable=stream_data
    )