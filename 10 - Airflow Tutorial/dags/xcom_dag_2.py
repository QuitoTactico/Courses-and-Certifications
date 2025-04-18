from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup

from random import uniform
from datetime import datetime

default_args = {"start_date": datetime(2020, 1, 1)}


def _training_model():
    accuracy = uniform(0.1, 10.0)
    print(f"model's accuracy: {accuracy}")


def _choose_best_model():
    print("choose best model")


with DAG(
    "xcom_dag_2", schedule_interval="@daily", default_args=default_args, catchup=False
) as dag:

    downloading_data = BashOperator(task_id="downloading_data", bash_command="sleep 3")

    with TaskGroup("processing_tasks") as processing_tasks:
        training_model_a = PythonOperator(
            task_id="training_model_a", python_callable=_training_model
        )

        training_model_b = PythonOperator(
            task_id="training_model_b", python_callable=_training_model
        )

        training_model_c = PythonOperator(
            task_id="training_model_c", python_callable=_training_model
        )

    choose_model = PythonOperator(task_id="task_4", python_callable=_choose_best_model)

    downloading_data >> processing_tasks >> choose_model
