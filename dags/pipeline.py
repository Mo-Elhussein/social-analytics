import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

#  load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "airflow")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")


def export_daily_csv():
    """CSV"""
    conn = psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT
    )
    query = "SELECT * FROM fct_daily_metrics;"
    df = pd.read_sql(query, conn)
    conn.close()

    output_path = "/opt/airflow/dags/output/daily_metrics.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ CSV Exported to {output_path}")


if __name__ == "__main__":
    export_daily_csv()
