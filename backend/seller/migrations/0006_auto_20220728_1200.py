# Generated by Django 3.2 on 2022-07-28 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0005_alter_seller_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='profile',
        ),
        migrations.AddField(
            model_name='seller',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
            preserve_default=False,
        ),
    ]
