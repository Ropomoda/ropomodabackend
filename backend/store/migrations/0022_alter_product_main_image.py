# Generated by Django 3.2 on 2022-07-29 02:48

from django.db import migrations, models
import store.utils


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20220729_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(upload_to=store.utils.product_main_image_path, verbose_name='main image'),
        ),
    ]
