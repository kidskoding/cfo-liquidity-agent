from utils.config import settings

def get_issuing_card_id(stripe_acct_id):
    query = f'''
        SELECT stripe_ic_id
        FROM {settings.db_table_path}
        WHERE stripe_acct_id = '{stripe_acct_id}'
        ORDER BY created_at DESC
        LIMIT 1
    '''
    
    try:
        res = settings.w.statement_execution.execute_statement(
            statement=query,
            warehouse_id=settings.warehouse_id
        )
        
        if res.result and res.result.data_array:
            ic_id = res.result.data_array[0][0]
            return ic_id
        
        print(f"no card linked for account: {stripe_acct_id}")
        return None
    except Exception as e:
        print(f"resolver error: {e}")
        return None