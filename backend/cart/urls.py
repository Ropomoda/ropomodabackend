from django.urls import path

from .views import *


urlpatterns = [
    path('', CartItemAPIView.as_view() , name="cart-list-create"),
    path('item/<uuid:uuid>', CartItemView.as_view() , name="cart-update-retrieve-delete"),
]
