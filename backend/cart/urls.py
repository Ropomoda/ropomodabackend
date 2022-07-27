from django.urls import path

from .views import *


urlpatterns = [
    path('', CartItemCreate.as_view() , name="cartItem-create"),
]
