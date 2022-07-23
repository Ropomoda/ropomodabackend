from .views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
]