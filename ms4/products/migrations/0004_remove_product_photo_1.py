# Generated by Django 2.2.12 on 2020-04-17 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_farm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo_1',
        ),
    ]