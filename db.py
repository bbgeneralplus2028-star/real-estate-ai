import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ.get("DATABASE_URL")


# -----------------------------
# SAFE CONNECTION HANDLER
# -----------------------------
def get_conn():
    """
    Returns a PostgreSQL connection safely.
    Never crashes the whole app during import.
    """
    try:
        if not DATABASE_URL:
            print("WARNING: DATABASE_URL not set")
            return None

        conn = psycopg2.connect(
            DATABASE_URL,
            cursor_factory=RealDictCursor
        )
        return conn

    except Exception as e:
        print(f"DB Connection Error: {e}")
        return None


# -----------------------------
# SAFE QUERY EXECUTOR
# -----------------------------
def run_query(query, params=None, fetch=False):
    """
    Safe database execution wrapper.
    Prevents crashes in production.
    """
    conn = get_conn()
    if conn is None:
        return None

    try:
        cur = conn.cursor()
        cur.execute(query, params or ())

        if fetch:
            result = cur.fetchall()
        else:
            result = None

        conn.commit()
        cur.close()
        conn.close()

        return result

    except Exception as e:
        print(f"Query Error: {e}")
        return None


# -----------------------------
# TEST FUNCTION (OPTIONAL)
# -----------------------------
def test_db():
    return run_query("SELECT 1 as test;", fetch=True)
