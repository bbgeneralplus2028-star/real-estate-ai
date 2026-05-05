from fastapi import FastAPI, Query
import os

# Stripe (optional but included)
import stripe

app = FastAPI(title="Real Estate AI SaaS")

# ----------------------------
# CONFIG
# ----------------------------
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "")

STRIPE_PRICE_ID = os.getenv("STRIPE_PRICE_ID", "")

# ----------------------------
# HEALTH CHECK
# ----------------------------
@app.get("/")
def home():
    return {
        "status": "real estate SaaS running",
        "version": "1.0"
    }

# ----------------------------
# REAL ESTATE AI (basic placeholder)
# ----------------------------
@app.get("/ai/search")
def ai_search(q: str = Query(...)):
    return {
        "query": q,
        "results": [
            {
                "title": "Modern Family Home",
                "price": 450000,
                "location": "New Jersey"
            },
            {
                "title": "Luxury Condo",
                "price": 780000,
                "location": "NYC"
            }
        ]
    }

# ----------------------------
# STRIPE CHECKOUT
# ----------------------------
@app.get("/subscribe")
def subscribe(email: str):

    if not stripe.api_key or not STRIPE_PRICE_ID:
        return {
            "error": "Stripe not configured",
            "hint": "Add STRIPE_SECRET_KEY and STRIPE_PRICE_ID in Render env vars"
        }

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": STRIPE_PRICE_ID,
            "quantity": 1
        }],
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
        customer_email=email
    )

    return {"checkout_url": session.url}
