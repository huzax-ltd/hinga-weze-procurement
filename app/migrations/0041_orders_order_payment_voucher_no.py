# Generated by Django 2.1.3 on 2019-03-31 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0040_auto_20190331_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_payment_voucher_no',
            field=models.CharField(blank=True, max_length=100, verbose_name='Voucher No.'),
        ),
    ]
