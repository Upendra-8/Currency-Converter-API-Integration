"""
This file contains the logic to interact with the external API to fetch exchange rates 
and perform currency conversions based on those rates. 
The CurrencyConverterService class includes methods for fetching exchange rates 
for a given base currency and converting amounts from one currency to another using those rates.
"""

import requests  # The requests library is used for making HTTP requests to external APIs

# The base URL of the external API that provides exchange rate data
API_URL = "https://api.exchangerate-api.com/v4/latest/"

class CurrencyConverterService:
    """
    A service class that handles fetching exchange rates for a given base currency 
    and performing currency conversion calculations.
    """
    
    @staticmethod
    def get_exchange_rates(base_currency="USD"):
        """
        Fetch the exchange rates for the given base currency from an external API.
        If no base currency is provided, it defaults to 'USD'.
        """
        try:
            # Make a GET request to the external API to fetch exchange rates for the base currency
            response = requests.get(f"{API_URL}{base_currency}")
            response.raise_for_status()  # Raise an HTTPError if the response code indicates an error
            data = response.json()  # Parse the JSON response to a Python dictionary
            return data['rates']  # Return the 'rates' dictionary from the API response
        except requests.exceptions.RequestException as e:
            # Catch any request errors (e.g., network failure) and raise a ValueError
            raise ValueError(f"Error fetching exchange rates: {e}")

    @staticmethod
    def convert_currency(from_currency, to_currency, amount, rates):
        """
        Convert the given amount from one currency to another using the provided exchange rates.
        The function checks if the 'from_currency' and 'to_currency' exist in the rates and 
        performs the conversion. If the currencies are the same, it returns the original amount.
        """
        if from_currency == to_currency:
            return amount  # If the currencies are the same, no conversion is needed, so return the original amount
        
        # Check if the provided currencies exist in the rates
        if from_currency not in rates or to_currency not in rates:
            raise ValueError("Invalid currency code(s) provided.")
        
        # Perform the conversion: Convert from 'from_currency' to 'to_currency'
        rate_from = rates[from_currency]
        rate_to = rates[to_currency]
        converted_amount = amount * rate_to / rate_from  # Formula for currency conversion
        return round(converted_amount, 2)  # Round the result to two decimal places
