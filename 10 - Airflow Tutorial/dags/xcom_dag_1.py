from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime


def _t1a():  # no necesita ti
    # forma 1
    # task_id = t1a
    # key = return_value  # queda este por default
    return 42


def _t1b(ti):
    # forma 2
    # task_id = t1b
    # key = my_key
    ti.xcom_push(key="my_key", value=30)


def _t2(ti):
    t1a_value = ti.xcom_pull(key="return_value", task_ids="t1a")

    t1b_value = ti.xcom_pull(key="my_key", task_ids="t1b")

    print(t1a_value, t1b_value)


with DAG(
    "xcom_dag_1",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t1a = PythonOperator(task_id="t1a", python_callable=_t1a)

    t1b = PythonOperator(task_id="t1b", python_callable=_t1b)

    t2 = PythonOperator(task_id="t2", python_callable=_t2)

    t3 = BashOperator(task_id="t3", bash_command="echo ''")

    [t1a, t1b] >> t2 >> t3
