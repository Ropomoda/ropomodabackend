# Generated by Django 3.2 on 2022-07-29 05:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='id',
        ),
        migrations.AlterField(
            model_name='cart',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
