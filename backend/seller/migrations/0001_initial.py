# Generated by Django 3.2 on 2022-07-30 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import seller.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('store_name', models.CharField(max_length=250)),
                ('logo', models.ImageField(blank=True, default=None, null=True, upload_to=seller.utils.seller_logo_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
            },
        ),
    ]
