from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Real Estate AI SaaS")

# -----------------------
# CORS (for frontend calls)
# -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# SERVE FRONTEND
# -----------------------
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# -----------------------
# AI SEARCH ENDPOINT
# -----------------------
@app.get("/api/search")
def search(q: str):
    return {
        "query": q,
        "results": [
            {"title": "Modern Family Home", "price": 450000, "location": "NJ"},
            {"title": "Luxury Condo", "price": 780000, "location": "NYC"},
            {"title": "Starter Home", "price": 320000, "location": "PA"}
        ]
    }

# -----------------------
# STATUS CHECK
# -----------------------
@app.get("/api/status")
def status():
    return {"status": "real estate SaaS running", "version": "1.1"}
