from __future__ import annotations  # Enable postponed evaluation of type annotations
import os
import json
from dotenv import load_dotenv
from app.settings import pax8_settings
from app.manager import Pax8Manager

# Load environment variables from the .env file
load_dotenv()

def main():
    # Initialize Pax8Settings from environment variables
    settings = pax8_settings(
        client_id=os.getenv("PAX8_CLIENT_ID"),
        client_secret=os.getenv("PAX8_CLIENT_SECRET"),
        audience=os.getenv("PAX8_AUDIENCE"),
        grant_type=os.getenv("PAX8_GRANT_TYPE"),
        base_url=os.getenv("PAX8_BASE_URL")
    )

    # Initialize Pax8Manager with the settings
    manager = Pax8Manager(settings)

    # Specify the company id you want to fetch details for.
    company_id = "your_company_id_here"  # Replace with a valid company id

    # Retrieve company details
    print("Fetching company details...")
    company_response = manager.get_company(company_id)
    if company_response.is_success:
        print("Company Details:")
        print(json.dumps(company_response.content, indent=2))
    else:
        print("Failed to retrieve company details:")
        if company_response.error:
            print(company_response.error)
        else:
            print(company_response.message)

    # Retrieve subscriptions related to the company
    print("\nFetching subscriptions for the company...")
    subscriptions_response = manager.get_subscription_by_company(company_id)
    if subscriptions_response.is_success:
        print("Subscriptions:")
        # Pretty-print the subscriptions data
        print(json.dumps(subscriptions_response.content, indent=2))
    else:
        print("Failed to retrieve subscriptions:")
        if subscriptions_response.error:
            print(subscriptions_response.error)
        else:
            print(subscriptions_response.message)

if __name__ == "__main__":
    main()
