# Generated by Django 3.2 on 2022-07-28 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_product_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_deleted',
        ),
    ]
