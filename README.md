# Social Analytics Pipeline

This project demonstrates a **data engineering pipeline** that ingests data from **YouTube** and **Reddit APIs**, 
stores raw data in Postgres, transforms it with **dbt**, and orchestrates the workflow using **Apache Airflow**.

---

## 📂 Project Structure

```
social-analytics/
│── dags/
│   └── social_pipeline_dag.py      # Airflow DAG that orchestrates the pipeline
│
│── dbt_project/                    # dbt project for transformations
│   └── models/
│       ├── stg_posts.sql           # Staging layer
│       ├── fct_daily_metrics.sql   # Daily metrics fact table
│       ├── top_posts.sql           # Top performing posts
│       └── moving_avg.sql          # Moving average metrics
│
│── ingestion.py                    # Functions to fetch data from YouTube & Reddit APIs
│── pipeline.py                     # Exports results into CSVs
│── docker-compose.yml              # Services (Postgres, Airflow, Adminer, etc.)
│── requirements.txt                # Python dependencies
│── dbt_requirements.txt            # dbt dependencies
│── .env                            # API keys and database connection details
```

---

## 🚀 Workflow

1. **Ingestion**
   - `ingestion.py` contains functions:
     - `ingest_youtube()`: Fetches videos metadata from YouTube API.
     - `ingest_reddit()`: Fetches subreddit posts from Reddit API.
   - Data is written into the Postgres database.

2. **Transformation**
   - dbt models under `dbt_project/models` run SQL transformations:
     - `stg_posts.sql` → raw staging layer.
     - `fct_daily_metrics.sql` → daily KPIs (views, likes, comments).
     - `top_posts.sql` → top N posts by engagement.
     - `moving_avg.sql` → rolling averages for trend analysis.

3. **Orchestration**
   - The Airflow DAG (`social_pipeline_dag.py`) orchestrates:
     - Run YouTube + Reddit ingestion in parallel.
     - Once complete, trigger the CSV export.

4. **Export**
   - `pipeline.py` collects transformed data and exports it into CSV for analytics / visualization.

---

## 🐳 Running with Docker

1. Copy your API keys into `.env` file:

```env
YOUTUBE_API_KEY=your_youtube_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=airflow
```

2. Start all services:

```bash
docker compose up --build
```

3. Access UIs:
   - Airflow: [http://localhost:8081](http://localhost:8081)
   - Adminer (Postgres UI): [http://localhost:8080](http://localhost:8080)

---

## 📊 Data Flow

```
YouTube API ─┐
             ├── ingestion.py ──> Postgres ──> dbt models ──> Analytics CSV (pipeline.py)
Reddit API ──┘
```

---

## ✅ Next Steps

- Add unit tests for ingestion functions.
- Extend dbt models with more advanced KPIs.
- Visualize the exported CSVs in tools like Tableau / PowerBI.

## Environment Variables

This project uses a `.env` file for sensitive credentials (API keys, DB passwords, etc.).  
The `.env` file is **excluded from Git** via `.gitignore` to avoid exposing secrets.

If you clone this repository, copy the provided `example.env` file to `.env` and fill in your own credentials:

```bash
cp example.env .env
