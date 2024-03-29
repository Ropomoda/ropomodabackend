"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

API_VERSION = getattr(settings, "API_VERSION", None)

admin.site.site_header = "Ropomoda Admin"
admin.site.site_title = "Ropomoda Admin"
admin.site.index_title = "Welcome to Ropomoda Admin"

urlpatterns = [
    path(f'{API_VERSION}/account/', include('account.urls')),
    path(f'{API_VERSION}/store/', include('store.urls')),
    path(f'{API_VERSION}/category/', include('category.urls')),
    path(f'{API_VERSION}/collection/', include('collection.urls')),
    path(f'{API_VERSION}/seller/', include('seller.urls')),
    path(f'{API_VERSION}/order/', include('order.urls')),
    path(f'{API_VERSION}/cart/', include('cart.urls')),
    path(f'{API_VERSION}/billing/', include('billing.urls')),


    
    path('', include('drfpasswordless.urls')),
    path('admin/', admin.site.urls),
]
