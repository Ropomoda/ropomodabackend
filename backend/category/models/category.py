from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/category/" , default="")
    parent = models.ForeignKey(
        'Category' ,
        on_delete=models.CASCADE,
        null=True ,
        blank=True ,
        default=None
    )
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    def __str__(self):
        return self.name
