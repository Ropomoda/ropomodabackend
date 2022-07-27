from .views import *

urlpatterns = [
    path('', OrderList.as_view() , name="order-list"),
]