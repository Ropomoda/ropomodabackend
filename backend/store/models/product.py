from django.db import models
from app.models import Extensions
from store.utils import product_image_path


class Product(Extensions):
    code = models.IntegerField(db_index=True , default=100000 )
    title_fa = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300 , default='')
    slug = models.CharField(unique=True , max_length=350)
    rrp_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    is_promotion = models.BooleanField(default=False)
    active_collection = models.ForeignKey('collection.Collection', 
        on_delete=models.CASCADE , 
        null=True , 
        blank=True , 
        default=None
    )
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to=product_image_path)
    seller = models.ForeignKey('seller.Seller' , on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

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
        return f'{self.title_fa} {self.code}'