from datetime import datetime

from airflow.decorators import dag, task

from include.scripts.upload_file_to_s3 import main_s3
from include.settings import settings


@dag(
    dag_id='upload_file_to_s3',
    schedule='*/5 * * * *',
    start_date=datetime(2025, 5, 27),
    catchup=False  # Backfill
)
def main():
    @task(task_id='main_s3')
    def task_main_s3(output_dir):
        return main_s3(output_dir)

    task_main_s3(settings.OUTPUT_DIR)


main()
