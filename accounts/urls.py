from django.urls import path

from accounts.views import *


urlpatterns = [
    path('login/', login_activation_code),
    path('login/send_activation_code/', send_activation_code),
]
