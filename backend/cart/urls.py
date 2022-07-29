from django.urls import path

from .views import *


urlpatterns = [
    path('', CartItemAPIView.as_view() , name="cart-list-create"),
    path('cart-item/<uuid:pk>', CartItemView.as_view() , name="cart-update-retrieve-delete"),
]
