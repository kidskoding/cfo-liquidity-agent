import stripe
import os

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

def get_pending_balance():
    balance = stripe.Balance.retrieve()
    return {
        "pending": balance["pending"],
        "available": balance["available"]
    }

def get_merchant_id():
    account = stripe.Account.retrieve()
    return {"merchant_id": account["id"]}
