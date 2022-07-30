# Generated by Django 3.2 on 2022-07-27 18:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20220726_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
