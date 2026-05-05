from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_conn():
    return psycopg2.connect(DATABASE_URL)

@app.get("/")
def home():
    return {"status": "real estate AI running"}

@app.post("/save")
def save_item():
    return {"message": "save endpoint working"}
