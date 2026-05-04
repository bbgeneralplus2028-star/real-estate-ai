from fastapi import FastAPI
from db import get_connection

app = FastAPI(title="Real Estate AI API")

@app.get("/")
def home():
    return {"status": "running", "message": "API is live"}

# -------------------------
# CREATE LISTING
# -------------------------
@app.post("/listings")
def create_listing(title: str, price: float, location: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO listings (title, price, location)
        VALUES (%s, %s, %s)
        RETURNING id;
        """,
        (title, price, location)
    )

    listing_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return {"id": listing_id, "status": "created"}

# -------------------------
# GET ALL LISTINGS
# -------------------------
@app.get("/listings")
def get_listings():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, title, price, location FROM listings;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {"id": r[0], "title": r[1], "price": r[2], "location": r[3]}
        for r in rows
    ]
