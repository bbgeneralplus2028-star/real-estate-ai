import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_checkout_session(email: str):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": os.getenv("STRIPE_PRICE_ID"),
            "quantity": 1,
        }],
        success_url="https://your-domain.com/success",
        cancel_url="https://your-domain.com/cancel",
        customer_email=email
    )

    return session.url
