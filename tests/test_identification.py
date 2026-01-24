import pytest
import uuid
from tools.linker import link_merchant_identification
from utils.config import settings

def test_databricks_connection():
    assert settings.w.clusters.list() is not None
    
def test_merchant_insertion():
    unique_id = str(uuid.uuid4())[:8]
    test_merchant = f"Test_Cafe_{unique_id}"
    test_acct = f"acct_{unique_id}"
    test_ic = f"ic_{unique_id}"
    
    link_merchant_identification(
        settings.w, 
        settings.warehouse_id, 
        test_merchant, 
        test_acct, 
        test_ic
    )
    
    query = f"SELECT * FROM registry.identification WHERE merchant_name = '{test_merchant}'"
    
    result = settings.w.statement_execution.execute_statement(
        statement=query,
        warehouse_id=settings.warehouse_id
    )
    
    assert result.result.data_array is not None
    assert len(result.result.data_array) > 0
    
    row = result.result.data_array[0]
    assert row[0] == test_merchant