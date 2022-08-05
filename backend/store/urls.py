from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductList.as_view() , name="product-list"),
    path('product/<int:code>/', ProductDetail.as_view() , name="product-detail"),
    path('product/<int:code>/variety/', VarietyList.as_view() , name="variety-list"),
    path('variety/<uuid:uuid>/', VarietyImageList.as_view() , name="variety-image-list"),
]