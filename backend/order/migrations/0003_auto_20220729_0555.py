# Generated by Django 3.2 on 2022-07-29 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20220729_0554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='orderrow',
            old_name='uuid',
            new_name='id',
        ),
    ]
