# Generated by Django 3.2 on 2022-07-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_title_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.AutoField(default=602940, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
