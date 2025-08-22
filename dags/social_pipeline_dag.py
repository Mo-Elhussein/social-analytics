from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


from ingestion import ingest_youtube, ingest_reddit
from pipeline import export_daily_csv  

default_args = {
    "owner": "social-analytics",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="social_pipeline",
    description="YouTube + Reddit ingestion then export daily CSV",
    default_args=default_args,
    start_date=datetime(2025, 8, 1),
    schedule_interval="0 9 * * *",  ## 9 am
    catchup=False,
    max_active_runs=1,
    tags=["social", "reddit", "youtube"],
) as dag:

    youtube_task = PythonOperator(
        task_id="ingest_youtube",
        python_callable=ingest_youtube,
    )

    reddit_task = PythonOperator(
        task_id="ingest_reddit",
        python_callable=ingest_reddit,
    )

    export_task = PythonOperator(
        task_id="export_daily_csv",
        python_callable=export_daily_csv,
    )


    [youtube_task, reddit_task] >> export_task
