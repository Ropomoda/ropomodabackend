# Generated by Django 4.0.5 on 2022-07-05 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='id',
            new_name='user',
        ),
    ]
