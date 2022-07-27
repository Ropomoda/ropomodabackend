from django.urls import path

from account.views import *


urlpatterns = [
    path('', UserDetail.as_view() , name="user-detail"),
    path('profile/', ProfileDetail.as_view() , name="profile-detail"),
    path('address/', AddressDetail.as_view() , name="address-detail"),
]
