from utils import gcp_secrets
import stripe

def main():
    stripe.api_key = gcp_secrets.get_gcp_secret("STRIPE_API_KEY")

if __name__ == "__main__":
    main()
