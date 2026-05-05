from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Real Estate AI SaaS")

# -------------------------
# API ROUTES FIRST
# -------------------------
@app.get("/api/status")
def status():
    return {"status": "real estate SaaS running", "version": "1.2"}

@app.get("/api/search")
def search(q: str):
    return {
        "query": q,
        "results": [
            {"title": "Modern Home", "price": 450000, "location": "NJ"},
            {"title": "Luxury Condo", "price": 780000, "location": "NYC"},
        ]
    }

# -------------------------
# SERVE FRONTEND SAFELY
# -------------------------
if os.path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def home():
    index_path = "frontend/index.html"
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "frontend not found"}
