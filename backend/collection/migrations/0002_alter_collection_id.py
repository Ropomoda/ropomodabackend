# Generated by Django 3.2 on 2022-07-27 18:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]