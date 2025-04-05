from airflow import DAG

# from airflow.providers.postgres.operators.postgres import PostgresOperator # deprecated
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.http.sensors.http import HttpSensor

# from airflow.providers.http.operators.http import HttpOperator # deprecated
from airflow.providers.http.operators.http import HttpOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

import json
from pandas import json_normalize
from datetime import datetime

# Connections
'''
Connection Id: postgres
Connection type: postgres
Host: postgres
Database: airflow
Login: airflow
Password: airflow
Port: 5432

Connection Id: user_api
Connection type: HTTP
Host: https://randomuser.me/

'''


# ti = task instance
def _process_user(ti):
    user = ti.xcom_pull(task_ids="extract_user")
    user = user["results"][0]
    processed_user = json_normalize(
        {
            "firstname": user["name"]["first"],
            "lastname": user["name"]["last"],
            "country": user["location"]["country"],
            "username": user["login"]["username"],
            "password": user["login"]["password"],
            "email": user["email"],
        }
    )
    processed_user.to_csv("/tmp/processed_user.csv", index=None, header=False)


def _store_user():
    # esto no estaba en el operator así que por eso usamos el hook
    hook = PostgresHook(postgres_conn_id="postgres")
    hook.copy_expert(
        sql="COPY users FROM stdin WITH DELIMITER as ','",
        filename="/tmp/processed_user.csv",
    )


with DAG(
    "user_processing",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # create_table = PostgresOperator( # deprecated
    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        # postgres_conn_id='postgres', # deprecated
        conn_id="postgres",
        sql="""
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            );
        """,
    )

    is_api_available = HttpSensor(
        task_id="is_api_available", http_conn_id="user_api", endpoint="api/"
    )

    # extract_user = SimpleHttpOperator( # deprecated
    extract_user = HttpOperator(
        task_id="extract_user",
        http_conn_id="user_api",
        endpoint="api/",
        method="GET",
        response_filter=lambda response: json.loads(response.text),
        log_response=True,
    )

    process_user = PythonOperator(
        task_id="process_user",
        python_callable=_process_user,
    )

    store_user = PythonOperator(
        task_id="store_user",
        python_callable=_store_user,
    )

    # dependencies
    create_table >> is_api_available >> extract_user >> process_user >> store_user
