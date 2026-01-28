import pytest
import stripe

from tools.card_manager import set_card_spending_limit

@pytest.fixture(scope="module")
def stripe_test_card():
    holder = stripe.issuing.Cardholder.create(
        name="Test Auditor Merchant",
        type="individual",
        billing={
            "address": {
                "line1": "123 Main St",
                "city": "SF",
                "state": "CA",
                "postal_code": "94105",
                "country": "US"
            }
        }
    )
    
    card = stripe.issuing.Card.create(
        cardholder=holder.id,
        currency="usd",
        type="virtual"
    )
    
    yield card
    
    stripe.issuing.Card.modify(card.id, status="inactive")

def test_spending_limit_flow(stripe_test_card):
    card_id = stripe_test_card.id
    
    result = set_card_spending_limit(card_id, 100, "daily")
    
    assert result is not None
    assert result.spending_controls.spending_limits[0].amount == 10000