from .views import *

urlpatterns = [
    path('', OrderAPIView.as_view() , name="order-list-create"),
    path('<uuid:pk>/', OrderView.as_view() , name="order-detail"),
    path('<uuid:pk>/item/', OrderRowAPIView.as_view() , name="order-list-create"),
]