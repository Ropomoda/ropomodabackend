# Generated by Django 3.2 on 2022-07-29 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220729_0554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='uuid',
            new_name='id',
        ),
    ]