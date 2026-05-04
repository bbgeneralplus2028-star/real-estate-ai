import os
import psycopg2
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

# -------------------------
# APP INIT (THIS WAS MISSING)
# -------------------------
app = FastAPI()

# -------------------------
# DATABASE CONNECTION
# -------------------------
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_conn():
    if not DATABASE_URL:
        return None
    return psycopg2.connect(DATABASE_URL)

# -------------------------
# SIMPLE FRONTEND (OPTIONAL)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Real Estate AI</title></head>
        <body>
            <h1>Real Estate AI API Running</h1>
            <p>Use /save endpoint to store data</p>
        </body>
    </html>
    """

# -------------------------
# SAVE DATA ENDPOINT
# -------------------------
@app.post("/save")
async def save_data(request: Request):
    data = await request.json()

    conn = get_conn()
    if conn is None:
        return JSONResponse({"error": "DATABASE_URL not set"}, status_code=500)

    cur = conn.cursor()

    # simple table-safe insert (you can expand later)
    cur.execute(
        "CREATE TABLE IF NOT EXISTS saved_data (id SERIAL PRIMARY KEY, data TEXT)"
    )

    cur.execute(
        "INSERT INTO saved_data (data) VALUES (%s)",
        (str(data),)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "saved", "data": data}
