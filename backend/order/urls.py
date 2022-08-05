from django.urls import path
from .views import *

urlpatterns = [
    path('', OrderAPIView.as_view() , name="order-list-create"),
    path('<uuid:uuid>/', OrderView.as_view() , name="order-detail"),
    path('<uuid:uuid>/item/', OrderRowAPIView.as_view() , name="order-list-create"),
]