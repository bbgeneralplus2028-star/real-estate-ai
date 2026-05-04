from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_conn():
    return psycopg2.connect(DATABASE_URL)

class Deal(BaseModel):
    purchase: float
    arv: float
    sqft: float
    condition: float
    months: float


@app.post("/analyze")
def analyze(deal: Deal):

    RC = deal.sqft * deal.condition
    EC = RC * 0.10
    TC = deal.months * 2000
    CC = (RC + EC) * 0.15

    TP = RC + EC + TC + CC
    total = deal.purchase + TP
    profit = deal.arv - total

    if profit > 80000:
        strategy = "FLIP"
    elif profit > 30000:
        strategy = "MINIMAL REHAB"
    elif profit > 0:
        strategy = "SECTION 8 / OWNER FINANCE"
    else:
        strategy = "WALK AWAY"

    return {
        "repair": RC,
        "equipment": EC,
        "holding": TC,
        "contingency": CC,
        "transformation": TP,
        "total": total,
        "profit": profit,
        "strategy": strategy
    }


@app.post("/save")
def save(data: dict):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO deals 
        (purchase, arv, profit, transformation_cost, strategy, risk_level)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        data.get("purchase", 0),
        data.get("arv", 0),
        data.get("profit", 0),
        data.get("transformation", 0),
        data.get("strategy", ""),
        "AUTO"
    ))

    conn.commit()
    conn.close()

    return {"status": "saved"}
