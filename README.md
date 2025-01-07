# Currency-Converter-API-Integration
## Overview
Welcome to the Currency Converter API! This Django REST Framework (DRF) application allows users to fetch real-time exchange rates and perform currency conversions. The application integrates with an external API to retrieve exchange rate data.

## Features
- Fetch Exchange Rates: Retrieve real-time exchange rates for a given base currency (default: USD).

- Currency Conversion: Convert a specified amount from one currency to another.
## Installation
## Prerequisites
Ensure you have the following installed:

- Python 3.x

- Django 3.x or higher

- Django REST Framework (DRF)

- Requests library

- An active internet connection (for fetching exchange rates).
## Setup
1. Clone the Repository
git clone https://github.com/yourusername/Currency-Converter-API-Integration
cd currency-converter
2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Apply Database Migrations
python manage.py migrate

## Running the Application
1. Start the Development Server
python manage.py runserver
2. Access the Application
Navigate to http://127.0.0.1:8000/ in your web browser or use tools like Postman for API testing.

**Stop the Server:**
Press Ctrl + C in the terminal to stop the server.

## Usage
You can use Postman to interact with the API.

**1. Fetch Exchange Rates**
- Endpoint: GET /api/rates

- Method: GET

- Query Parameters:

    - base (optional): The base currency code (e.g., USD, EUR). Defaults to USD.

**Example Request in Postman:**

1. Open Postman and create a new GET request.

2. Enter the URL: http://127.0.0.1:8000/api/rates?base=EUR

3. Click Send.

**Example Response:**

{

    "USD": 1.0,
    
    "EUR": 0.85,
    
    "GBP": 0.75,
    
    "JPY": 110.0
    
}

**2. Convert Currency**
- Endpoint: POST /api/convert

- Method: POST

- Body:

    - from (string): The source currency code (e.g., USD).

    - to (string): The target currency code (e.g., EUR).

    - amount (float): The amount to convert.

  **Example Request in Postman:**

1. Open Postman and create a new POST request.

2. Enter the URL: http://127.0.0.1:8000/api/convert

3. Go to the Body tab and select raw and choose JSON from the dropdown.

4. Enter the following JSON in the body:

{

    "from": "USD",
    
    "to": "EUR",
    
    "amount": 100

}

5. Click Send.

**Example Response:**

{

    "from": "USD",
    
    "to": "EUR",
    
    "amount": 100,
    
    "convertedAmount": 85.0

}

## URL Patterns

- /api/rates: Fetch exchange rates for a base currency.
- /api/convert: Convert a specified amount from one currency to another.
## Contributing

We welcome contributions to improve the project. To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push your branch (git push origin feature-branch).
6. Open a Pull Request.
   
## Acknowledgments
- **Django REST Framework:** Used for building the API endpoints.

- **ExchangeRate API:** Provides real-time exchange rate data.
