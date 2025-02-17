from django.urls import path
from .views import get_transactions, sample_api

urlpatterns = [
    path("", get_transactions, name="transactions"),
    path('api/', sample_api),

]