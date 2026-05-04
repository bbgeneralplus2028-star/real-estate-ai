from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()   # 👈 MUST BE FIRST

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_conn():
    if not DATABASE_URL:
        return None
    return psycopg2.connect(DATABASE_URL)


@app.post("/save")
def save(data: dict):
    return {"status": "ok"}
@app.post("/save")
def save(data: dict):

    run_query("""
    INSERT INTO deals (purchase, arv, profit, transformation_cost, strategy, risk_level)
    VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        data.get("purchase",0),
        data.get("arv",0),
        data.get("profit",0),
        data.get("transformation",0),
        data.get("strategy",""),
        "AUTO"
    ))

    return {"status": "saved"}
