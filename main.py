from utils import gcp_secrets
import stripe

def main():
    stripe.api_key = gcp_secrets.get_stripe_key()

if __name__ == "__main__":
    main()
