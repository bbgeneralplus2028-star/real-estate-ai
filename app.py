from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import psycopg2

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")


# -----------------------
# DB CONNECTION
# -----------------------
def get_conn():
    return psycopg2.connect(DATABASE_URL)


# -----------------------
# MODELS
# -----------------------
class Property(BaseModel):
    address: str
    city: str
    state: str
    price: float
    beds: int
    baths: int
    sqft: int


class Lead(BaseModel):
    name: str
    email: str
    phone: str
    message: str
    property_id: int


# -----------------------
# HEALTH CHECK
# -----------------------
@app.get("/")
def home():
    return {"status": "real estate SaaS running"}


# -----------------------
# ADD PROPERTY
# -----------------------
@app.post("/properties")
def add_property(p: Property):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO properties (address, city, state, price, beds, baths, sqft)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (p.address, p.city, p.state, p.price, p.beds, p.baths, p.sqft))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "property added"}


# -----------------------
# GET PROPERTIES
# -----------------------
@app.get("/properties")
def get_properties():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM properties ORDER BY id DESC")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"data": rows}


# -----------------------
# LEADS
# -----------------------
@app.post("/leads")
def add_lead(l: Lead):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO leads (name,email,phone,message,property_id)
        VALUES (%s,%s,%s,%s,%s)
    """, (l.name, l.email, l.phone, l.message, l.property_id))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "lead captured"}


# -----------------------
# SIMPLE AI VALUATION
# -----------------------
@app.post("/ai/value")
def value_property(p: Property):

    base = p.price
    sqft_value = p.sqft * 180
    bed_bonus = p.beds * 15000
    bath_bonus = p.baths * 10000

    estimated = (sqft_value + bed_bonus + bath_bonus) / 2

    return {
        "estimated_value": round(estimated, 2),
        "logic": "basic AI model v1"
    }
