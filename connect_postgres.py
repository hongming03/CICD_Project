import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    return conn


# Not needed, table will be initialized when running docker compose via db/init.sql
# def create_table():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS urls (
#             id SERIAL PRIMARY KEY,
#             original_url TEXT NOT NULL,
#             short_code TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     cur.close()
#     conn.close()


def add_url(original_url, short_code):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO urls (original_url, short_code)
        VALUES (%s, %s)
    """,
        (original_url, short_code),
    )
    conn.commit()
    cur.close()
    conn.close()
