""" 
This file contains API views for handling requests related to currency conversion and fetching exchange rates. 
The views interact with services to get exchange rate data and perform currency conversion based on user input. 
The views use Django Rest Framework's (DRF) APIView and serializers to handle incoming data and return responses. 
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .services import CurrencyConverterService  # Service class to interact with the external API and convert currencies
from .serializers import CurrencyConversionSerializer  # Serializer class to validate currency conversion request data

class GetRates(APIView):
    """
    Handles GET requests for fetching exchange rates for a given base currency.
    The default base currency is USD if no base currency is provided in the query.
    """
    def get(self, request):
        base_currency = request.query_params.get('base', 'USD')  # Retrieve the base currency from query params (default to 'USD')
        try:
            # Fetch exchange rates from the CurrencyConverterService
            rates = CurrencyConverterService.get_exchange_rates(base_currency)
            return Response(rates, status=status.HTTP_200_OK)  # Return rates in the response
        except ValueError as e:
            raise ValidationError(str(e))  # Raise a ValidationError if fetching exchange rates fails


class ConvertCurrency(APIView):
    """
    Handles POST requests to convert a specified amount of currency from one to another.
    The request must provide 'from', 'to' currency codes and an 'amount'.
    """
    def post(self, request):
        # Validate and deserialize the incoming data using the CurrencyConversionSerializer
        serializer = CurrencyConversionSerializer(data=request.data)
        if serializer.is_valid():
            # Extract validated data from the serializer
            # The 'validated_data' is the data that has passed the serializer's validation checks.
            # The 'from' and 'to' fields represent the source and target currencies respectively,
            # and 'amount' is the amount of money to be converted.

            # Convert 'from' currency to uppercase to ensure consistency and to match the required currency code format (e.g., USD, EUR).
            from_currency = serializer.validated_data['from'].upper()

            # Convert 'to' currency to uppercase for the same reasons, ensuring it matches the expected format.
            to_currency = serializer.validated_data['to'].upper()

            # Extract the 'amount' to be converted from the validated data, no changes are needed here as it's a numerical value.
            amount = serializer.validated_data['amount']


            try:
                # Fetch exchange rates for the 'from_currency'
                rates = CurrencyConverterService.get_exchange_rates(from_currency)
                # Convert the amount using the CurrencyConverterService
                converted_amount = CurrencyConverterService.convert_currency(
                    from_currency, to_currency, amount, rates
                )
                # Return the conversion result
                return Response({
                    "from": from_currency,
                    "to": to_currency,
                    "amount": amount,
                    "convertedAmount": converted_amount
                }, status=status.HTTP_200_OK)
            except ValueError as e:
                raise ValidationError(str(e))  # Raise a ValidationError if the conversion fails
        
        # Return validation errors if the incoming data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
