# Generated by Django 2.1.3 on 2019-03-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0033_auto_20190330_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory_items',
            name='inventory_item_product_code',
            field=models.CharField(default=None, max_length=8, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='product_request_items',
            name='product_request_item_product_code',
            field=models.CharField(default=None, max_length=8, verbose_name='Code'),
        ),
    ]