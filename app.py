from fastapi import FastAPI
import os

app = FastAPI()

# Basic health check (Render needs this kind of endpoint to confirm app is alive)
@app.get("/")
def home():
    return {"status": "running"}

# Example POST endpoint
@app.post("/save")
def save_data():
    return {"message": "Save endpoint working"}
