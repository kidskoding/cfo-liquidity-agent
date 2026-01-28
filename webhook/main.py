import stripe
import os
import json
from flask import Flask, request, abort
from google.cloud import pubsub_v1

app = Flask(__name__)

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
WEBHOOK_SECRET = os.environ["STRIPE_WEBHOOK_SECRET"]

publisher = pubsub_v1.PublisherClient()
TOPIC_PATH = os.environ["PUBSUB_TOPIC"]

@app.route("/stripe/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, WEBHOOK_SECRET
        )
    except Exception:
        abort(400)

    if event["type"] == "payment_intent.succeeded":
        pi = event["data"]["object"]

        publisher.publish(
            TOPIC_PATH,
            json.dumps({
                "payment_intent_id": pi["id"],
                "account": event.get("account")  # present for Stripe Connect
            }).encode("utf-8")
        )

    return "", 200
