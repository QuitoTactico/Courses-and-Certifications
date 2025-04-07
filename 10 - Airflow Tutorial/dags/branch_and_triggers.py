from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from random import randint
from datetime import datetime


def _t1a():  # no necesita ti
    # forma 1
    # task_id = t1a
    # key = return_value  # queda este por default
    return randint(10, 40)


def _t1b(ti):
    # forma 2
    # task_id = t1b
    # key = my_key
    ti.xcom_push(key="my_key", value=30)


def _t2(ti):
    t1a_value = ti.xcom_pull(key="return_value", task_ids="t1a")

    t1b_value = ti.xcom_pull(key="my_key", task_ids="t1b")

    print("t1a:", t1a_value, "t1b:", t1b_value)


# retorna el task_id que le de la gana, y se sigue con esa
def _branch(ti):
    t1a_value = ti.xcom_pull(key="return_value", task_ids="t1a")

    t1b_value = ti.xcom_pull(key="my_key", task_ids="t1b")

    # return 't3' if (t1a_value < t1b_value) else 't4'
    if t1a_value < t1b_value:
        return "t3"
    return "t4"


with DAG(
    "branch_and_triggers",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    t1a = PythonOperator(task_id="t1a", python_callable=_t1a)

    t1b = PythonOperator(task_id="t1b", python_callable=_t1b)

    t2 = PythonOperator(task_id="t2", python_callable=_t2)

    branch = BranchPythonOperator(task_id="branch", python_callable=_branch)

    t3 = BashOperator(task_id="t3", bash_command="echo ''")

    t4 = BashOperator(task_id="t4", bash_command="echo ''")

    t5 = BashOperator(task_id="t5", bash_command="echo ''")

    t6 = BashOperator(task_id="t6", bash_command="echo ''", trigger_rule="one_success")

    # parece que no se puede así
    # [t1a, t1b] >> t2 >> branch >> [(t3 >> t5), t4] >> t6

    # así sí
    [t1a, t1b] >> t2 >> branch
    branch >> t3 >> t5 >> t6
    branch >> t4 >> t6
