import pytest
from tools.resolver import get_issuing_card_id
from utils.config import settings

def test_resolver_finds_existing_card():
    test_acct = "acct_b65e4fd0"
    
    print(f"testing resolver for: {test_acct}")
    
    ic_id = get_issuing_card_id(test_acct)
    
    assert ic_id is not None, f"Resolver failed to find {test_acct}"
    assert ic_id.startswith("ic_"), f"Returned ID {ic_id} doesn't look like a Stripe Card ID"
    
    print(f'success! resolved {test_acct} to {ic_id}')
    
def test_resolver_handles_missing_account():
    fake_acct = "acct_NONEXISTENT_123"
    ic_id = get_issuing_card_id(fake_acct)
    
    assert ic_id is None