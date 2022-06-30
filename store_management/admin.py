from django.contrib import admin

from .models.product import *


admin.site.register(Product)
admin.site.register(Category)
