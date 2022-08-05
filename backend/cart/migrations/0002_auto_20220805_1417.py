# Generated by Django 3.2 on 2022-08-05 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_variety_seller'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variety',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.variety'),
            preserve_default=False,
        ),
    ]
