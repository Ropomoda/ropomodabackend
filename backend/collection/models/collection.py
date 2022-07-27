from django.db import models

from app.models import BaseUUIDModel

from collection.utils import collection_image_path

class Collection(BaseUUIDModel):
    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"
    title_fa = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300 , default='')
    slug = models.CharField(unique=True , max_length=350)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to=collection_image_path)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.title_fa}" 
