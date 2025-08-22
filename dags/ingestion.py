# ingestion.py
# ----------------------------------------------------
# This module simulates ingestion of data from YouTube 
# and Reddit. Instead of calling real APIs, we use 
# mock data for testing & development.
# ----------------------------------------------------

import pandas as pd
from sqlalchemy import create_engine

# Database connection string (Postgres)
DB_CONN = "postgresql+psycopg2://postgres:postgres@postgres:5432/postgres"

def ingest_youtube():
    """
    Simulate ingestion of YouTube data.
    Creates a DataFrame with mock data and loads it into Postgres.
    """
    print("📥 Ingesting mock YouTube data...")

    data = {
        "video_id": ["yt1", "yt2", "yt3"],
        "title": ["Video A", "Video B", "Video C"],
        "views": [100, 250, 400],
        "likes": [10, 40, 60],
        "comments": [2, 6, 15],
    }

    df = pd.DataFrame(data)

    engine = create_engine(DB_CONN)
    df.to_sql("youtube_posts", engine, if_exists="replace", index=False)

    print("✅ YouTube ingestion completed.")


def ingest_reddit():
    """
    Simulate ingestion of Reddit data.
    Creates a DataFrame with mock data and loads it into Postgres.
    """
    print("📥 Ingesting mock Reddit data...")

    data = {
        "post_id": ["r1", "r2", "r3"],
        "title": ["Post A", "Post B", "Post C"],
        "upvotes": [15, 30, 50],
        "comments": [3, 8, 12],
    }

    df = pd.DataFrame(data)

    engine = create_engine(DB_CONN)
    df.to_sql("reddit_posts", engine, if_exists="replace", index=False)

    print("✅ Reddit ingestion completed.")
