from .views import *

urlpatterns = [
    path('product/', ProductList.as_view() , name="product-list"),
    path('product/<int:code>', ProductDetail.as_view() , name="product-detail"),
]