from fastapi import FastAPI

from app.routes import users, properties, leads, ai

app = FastAPI(title="Real Estate AI SaaS")

app.include_router(users.router)
app.include_router(properties.router)
app.include_router(leads.router)
app.include_router(ai.router)


@app.get("/")
def home():
    return {"status": "production SaaS running"}
