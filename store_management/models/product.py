from django.db import models
from django.db import models
from .category import Category


class Product(models.Model):
    code = models.IntegerField(unique=True , default=100000)
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, default=1)
    description = models.TextField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/' )

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name
