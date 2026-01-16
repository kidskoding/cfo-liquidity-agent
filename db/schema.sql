-- Identification Table
CREATE TABLE IF NOT EXISTS liquidity_agent_dev.registry.identification (
  merchant_name STRING,
  stripe_acct_id STRING,
  stripe_ic_id STRING,
  created_at TIMESTAMP
);