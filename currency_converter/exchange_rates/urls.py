"""
This file defines the URL routing for the API views in this application.
It maps specific URLs to the corresponding view classes, which handle the logic for fetching exchange rates and converting currencies.
"""

from django.urls import path  # Import Django's path function for URL routing
from .views import GetRates, ConvertCurrency  # Import the view classes for rates and conversion

# URL patterns for the 'GetRates' and 'ConvertCurrency' views
urlpatterns = [
    path('api/rates', GetRates.as_view(), name='get_rates'),  # URL for fetching exchange rates
    path('api/convert', ConvertCurrency.as_view(), name='convert_currency'),  # URL for converting currencies
]
