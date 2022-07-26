from .views import *

urlpatterns = [
    path('product/', ProductList.as_view() , name="product-list"),
]