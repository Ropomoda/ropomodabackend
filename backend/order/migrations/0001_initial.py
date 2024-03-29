# Generated by Django 3.2 on 2022-07-30 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('status', models.IntegerField(choices=[(0, 'INITIATED'), (3, 'ACCEPTED_PROCESSING'), (6, 'DELIVERED_POSTOFFICE'), (9, 'DELIVERY_AGENT_SENT'), (11, 'DELIVERY_CUSTOMER'), (12, 'CANCELED_BY_USER'), (13, 'CANCELED_BY_SELLER'), (14, 'CANCELED_BY_SELLER')], default=0)),
                ('payment_method', models.IntegerField(choices=[(0, 'ZARRIN_PAL'), (1, 'COD')])),
                ('is_payed', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.address')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name': 'OrderRow',
                'verbose_name_plural': 'OrderRows',
            },
        ),
    ]
