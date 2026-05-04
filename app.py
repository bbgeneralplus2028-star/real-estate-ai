import os
import psycopg2
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Create FastAPI app FIRST (this fixes your error)
app = FastAPI()

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_conn():
    if not DATABASE_URL:
        return None
    return psycopg2.connect(DATABASE_URL)

# ---------------------------
# ROUTES
# ---------------------------

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/save")
async def save_data(request: Request):
    data = await request.json()

    conn = get_conn()
    if conn is None:
        return JSONResponse(
            {"error": "DATABASE_URL not set"},
            status_code=500
        )

    try:
        cur = conn.cursor()

        # Example table insert (adjust to your schema)
        cur.execute(
            "INSERT INTO saved_data (payload) VALUES (%s)",
            (str(data),)
        )

        conn.commit()
        cur.close()
        conn.close()

        return {"status": "saved", "data": data}

    except Exception as e:
        return JSONResponse(
            {"error": str(e)},
            status_code=500
        )
