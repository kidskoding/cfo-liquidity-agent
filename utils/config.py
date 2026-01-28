import os
from dotenv import load_dotenv
from google.cloud import secretmanager
from databricks.sdk import WorkspaceClient
import stripe

load_dotenv()

class Config:
    def __init__(self):
        self.project_id = os.getenv("GCP_PROJECT_ID")
        if not self.project_id:
            raise ValueError("GCP_PROJECT_ID not found in .env file!")
            
        self.client = secretmanager.SecretManagerServiceClient()
        
        secret_keys = [
            "DATABRICKS_HOST",
            "DATABRICKS_TOKEN",
            "DATABRICKS_WAREHOUSE_ID",
            "DATABRICKS_TABLE_PATH",
            "STRIPE_API_KEY"
        ]
        
        self.values = self.load_secrets(secret_keys)
        
        self.db_host = self.values.get("DATABRICKS_HOST")
        self.db_token = self.values.get("DATABRICKS_TOKEN")
        self.warehouse_id = self.values.get("DATABRICKS_WAREHOUSE_ID")
        self.db_table_path = self.values.get("DATABRICKS_TABLE_PATH")
        
        self.w = WorkspaceClient(
            host=self.db_host,
            token=self.db_token
        )
        
        self.stripe_key = self.values.get("STRIPE_API_KEY")
        stripe.api_key = self.stripe_key
        
    def load_secrets(self, keys):
        secrets = {}
        for key in keys:
            name = f"projects/{self.project_id}/secrets/{key}/versions/latest"
            payload = self.client.access_secret_version(request={"name": name}).payload.data.decode("UTF-8")
            secrets[key] = payload
        return secrets

settings = Config()

def get_gcp_secret(secret_id):
    return settings.values.get(secret_id)