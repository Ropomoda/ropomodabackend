from app.models import Extensions
from django.db import models
from store.utils import product_image_path



class Color(Extensions):
    title_fa = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    hex_code = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.title_fa} {self.hex_code}'

class Size(Extensions):
    title_fa = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title_fa}'


class Variety(Extensions):
    class Meta:
        verbose_name_plural = "Varieties"
    color = models.ManyToManyField('store.Color')
    size = models.ManyToManyField('store.Size')
    rrp_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    selling_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    max_quantity = models.IntegerField(default=1)
    seller = models.ForeignKey('seller.Seller' , default=None, on_delete=models.RESTRICT)
    product = models.ForeignKey('store.Product', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.uuid} {self.product.title_fa}'

class VarietyImage(Extensions):
    title_fa = models.CharField(max_length=300, default='تصویر محصول')
    title_en = models.CharField(max_length=300 , default='product image')
    url = models.ImageField(verbose_name="image",upload_to=product_image_path)
    variety = models.ForeignKey('Variety', default=None, on_delete=models.RESTRICT)
    def __str__(self):
        return f'{self.uuid} {self.product.title_fa}'