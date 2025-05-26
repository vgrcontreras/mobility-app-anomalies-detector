from airflow.decorators import dag, task
from include.scripts.gerar_vendas import gerar_item, gerar_venda, gerar_jsonl

from datetime import datetime

OUTPUT_DIR = "/usr/local/airflow/include/data"

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
    
    t1 = task_gerar_jsonl(OUTPUT_DIR)
    
main()