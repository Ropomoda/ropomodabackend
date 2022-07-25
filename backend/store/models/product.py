from django.db import models


class Product(models.Model):
    code = models.AutoField(unique=True , default=602940 , primary_key=True)
    title_fa = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300 , default='')
    slug = models.CharField(unique=True , max_length=350)
    rrp_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to="images/store/")
    is_deleted = models.BooleanField(default=False , blank=True , null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

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
