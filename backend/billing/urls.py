from django.urls import path
from .views import *

urlpatterns = [
    path('purchase/order/<uuid:uuid>', PurchaseAPIView.as_view() , name="purchase"),
]