import pytest
import uuid
from tools.linker import link_merchant_identification
from utils.config import settings
from databricks.sdk.service.sql import StatementState

def test_databricks_connection():
    assert settings.w.clusters.list() is not None

# TEST WILL FAIL IF DATABRICKS IS NOT RUNNING!
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
    
    table_path = settings.db_table_path
    query = f"SELECT * FROM {table_path} WHERE merchant_name = '{test_merchant}'"
    
    result = settings.w.statement_execution.execute_statement(
        statement=query,
        warehouse_id=settings.warehouse_id
    )
    
    if result.status.state != StatementState.SUCCEEDED:
        pytest.fail(f"test failed: [{result.status.error.error_code}]: {result.status.error.message}")
    
    assert result.result.data_array is not None