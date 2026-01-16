import os
from google.cloud import secretmanager
from dotenv import load_dotenv

load_dotenv()

def get_stripe_key():
    project_id = os.getenv("GCP_PROJECT_ID")
    if not project_id:
        raise ValueError('GCP_PROJECT_ID is not found in environment variables!')
    
    client = secretmanager.SecretManagerServiceClient()
    name = f'projects/{project_id}/secrets/STRIPE_API_KEY/versions/latest'
    
    try:
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
    except Exception as e:
        print(f"error accessing GCP Secret: {e}")
        return None
    