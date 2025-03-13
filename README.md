# Pax8 API Manager

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Pax8 API Manager is a Python project designed to integrate with the Pax8 subscription management API. It handles authentication via OAuth2, retrieves company, product, and subscription details, and allows you to update subscriptions as needed. This project is structured to provide a clean, modular, and scalable codebase.

## Project Structure
```
.
├── app
│   ├── enums
│   │   └── BillingTerm.py
│   ├── manager
│   │   ├── __init__.py
│   │   ├── Pax8Manager.py
│   │   └── pax8_manager.py
│   ├── models
│   │   ├── request
│   │   │   └── SubscriptionRequest.py
│   │   └── response
│   │       ├── __init__.py
│   │       ├── company_response.py
│   │       ├── error_response.py
│   │       ├── page_response.py
│   │       ├── product_response.py
│   │       ├── response.py
│   │       ├── subscription_response.py
│   │       └── token_response.py
│   └── settings
│       ├── __init__.py
│       └── pax8_settings.py
├── tests
│   ├── __init__.py
│   ├── test_manager.py
│   ├── test_settings.py
│   └── test_token.py
├── venv
│   └── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/pax8-api-manager.git
   cd pax8-api-manager
   ```

2. **Create a Virtual Environment**
   Create an isolated Python environment:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - **On Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file (you can place it at the project root or inside your virtual environment directory) with the following contents:
   ```dotenv
   PAX8_AUDIENCE=api://p8p.client
   PAX8_BASE_URL=https://api.pax8.com/v1
   PAX8_CLIENT_ID=your_client_id
   PAX8_CLIENT_SECRET=your_client_secret
   PAX8_GRANT_TYPE=client_credentials
   ```
   Replace `your_client_id` and `your_client_secret` with your actual credentials.

## Usage

The main application is run via the `main.py` file. This file initializes the Pax8Manager, handles token authentication, retrieves company details, and fetches all subscriptions for a given company.

To run the application:
```bash
python main.py
```

Inside `main.py`, you’ll find an example code on how to use the manager. 

## Testing

Tests are located in the `tests` directory and use `pytest` as the testing framework. To run the tests, execute:
```bash
pytest
```
This command will discover and run all test files (e.g., `test_manager.py`, `test_settings.py`, `test_token.py`).

## Contributing

Contributions are welcome. Follow these steps to contribute:
1. **Fork the Repository**
2. **Create a New Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes**
   ```bash
   git commit -am "Description of your changes"
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a Pull Request**
   Provide a clear description of your changes and reference any related issues.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ClaudiaOM/Pax8Manager/blob/main/LICENSE.txt) file for details.

---

Happy coding!
