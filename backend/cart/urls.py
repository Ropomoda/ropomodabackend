from django.urls import path

from .views import *


urlpatterns = [
    path('', CartItemAPIView.as_view() , name="cartItem-view"),
]
