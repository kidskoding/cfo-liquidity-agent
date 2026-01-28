import stripe

def set_card_spending_limit(card_id: str, amt: int, interval: str = "all_time"):
    amount_in_cents = amt * 100
    
    try:
        updated_card = stripe.issuing.Card.modify(
            card_id,
            spending_controls={
                "spending_limits": [ 
                    {
                        "amount": amount_in_cents,
                        "interval": interval
                    }
                ]
            }
        )
        
        return updated_card
    except stripe.StripeError as e:
        print(f'Card Error: {e.user_message}')
        return None