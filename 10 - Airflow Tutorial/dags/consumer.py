from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")

# en este, se ejecuta cada que my_file es modificado
with DAG(
    dag_id="consumer",
    schedule=[my_file],
    start_date=datetime(2022, 1, 1),
    catchup=False,
):

    @task  # sin outlet porque esto no modifica nada
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print(f.read())

    read_dataset()
