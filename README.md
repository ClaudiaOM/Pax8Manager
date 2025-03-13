# Pax8 API Integration

## Overview
This project provides an integration with the Pax8 API, enabling the management of companies, products, and subscriptions through an easy-to-use Python application. The implementation leverages OAuth2 for secure authentication and follows clean coding principles to ensure scalability and maintainability.

---

## Features
- **Authentication**: Retrieve and refresh OAuth2 access tokens securely.
- **Company Management**:
  - Fetch paginated lists of companies.
  - Retrieve detailed information about a specific company.
- **Product Management**:
  - Fetch paginated lists of products.
  - Retrieve details of a specific product.
- **Subscription Management**:
  - Fetch paginated lists of subscriptions.
  - Retrieve subscriptions for a specific company.
  - Retrieve or update details of a specific subscription.

---

## Project Structure
```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── manager.py             # Contains the Pax8Manager class
│   ├── settings.py            # Handles Pax8Settings configuration
├── models/
│   ├── __init__.py
│   ├── request.py             # Request models (e.g., SubscriptionRequest)
│   ├── response.py            # Response models (e.g., TokenResponse, CompanyResponse)
├── .env                       # Environment variables (API keys, secrets, etc.)
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation for the project
└── main.py                    # Entry point for running the application
