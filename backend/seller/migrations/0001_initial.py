# Generated by Django 3.2 on 2022-07-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('logo', models.ImageField(upload_to='images/seller/')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
            },
        ),
    ]