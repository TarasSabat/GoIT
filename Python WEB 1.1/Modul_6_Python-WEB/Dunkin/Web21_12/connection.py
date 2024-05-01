import sqlite3
from contextlib import contextmanager
import os
from typing import Generator

from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import connection


load_dotenv()

pg_pass = os.getenv("POSTGRES_PASS")
pg_host = os.getenv("POSTGRES_HOST")

database = './example.db'

dsn_str = f"host={pg_host} dbname=postgres user=postgres password={pg_pass}"

@contextmanager
def create_connection(db_file, is_postgres=True) -> Generator[connection]:
    """ create a database connection to a SQLite database """
    if is_postgres:
        conn = psycopg2.connect(dsn_str)
    else:
        conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()
