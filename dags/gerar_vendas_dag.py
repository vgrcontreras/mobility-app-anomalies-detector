from datetime import datetime

from airflow.decorators import dag, task

from include.scripts.gerar_vendas import gerar_jsonl
from include.settings import settings


@dag(
    dag_id='gerar_vendas',
    schedule='* * * * *',
    start_date=datetime(2025, 5, 26),
    catchup=False  # backfill
)
def main():

    @task(task_id='gerar_jsonl')
    def task_gerar_jsonl(output_dir):
        return gerar_jsonl(output_dir)

    task_gerar_jsonl(settings.OUTPUT_DIR)


main()
