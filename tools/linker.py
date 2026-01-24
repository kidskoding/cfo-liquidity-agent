def link_merchant_identification(w, warehouse_id, merchant_name, acct_id, ic_id):
    query = f"""
        INSERT INTO registry.identification (merchant_name, stripe_acct_id, stripe_ic_id, created_at)
        VALUES ('{merchant_name}', '{acct_id}', '{ic_id}', CURRENT_TIMESTAMP())
    """
    
    try:
        w.statement_execution.execute_statement(
            statement=query,
            warehouse_id=warehouse_id
        )
        
        print(f"success {merchant_name} is now linked!")
    except Exception as e:
        print(f"error: {e}")