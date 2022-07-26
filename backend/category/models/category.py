from django.db import models
from mptt.models import MPTTModel , TreeForeignKey

from category.utils import category_image_path


class Category(MPTTModel):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=category_image_path, default="")
    parent = TreeForeignKey(
        'self' ,
        on_delete=models.CASCADE,
        null=True ,
        blank=True ,
        default=None,
        related_name="children"
    )
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    def __str__(self):
        return self.name
