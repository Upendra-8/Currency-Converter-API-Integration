"""
This file contains the serializer for the Currency Conversion API. 
The serializer validates and deserializes the input data for currency conversion requests. 
It ensures that the 'from', 'to' currency codes are valid and the 'amount' field is a float.
"""

from rest_framework import serializers  # Import DRF's serializers to create validation classes

class CurrencyConversionSerializer(serializers.Serializer):
    """
    Serializer class that validates and deserializes incoming data for currency conversion requests.
    It expects 'from' and 'to' currency codes (3-letter ISO 4217 codes) and an 'amount' field (float).
    """
    from_currency = serializers.CharField(max_length=3, source='from')  # Source is 'from' in the request payload
    to_currency = serializers.CharField(max_length=3, source='to')  # Source is 'to' in the request payload
    amount = serializers.FloatField()  # The amount to convert
