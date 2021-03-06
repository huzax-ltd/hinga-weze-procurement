# Generated by Django 2.1.3 on 2019-03-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0007_auto_20190316_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_items',
            name='order_item_currency',
            field=models.CharField(choices=[('', '--select--'), ('USD', 'Usd'), ('RWF', 'Rwf')], default='RWF',
                                   max_length=255, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='order_items',
            name='order_item_duration',
            field=models.IntegerField(default=0, verbose_name='Time in Days'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_project_code',
            field=models.CharField(blank=True, max_length=100, verbose_name='Project Code'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_requisition_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='Requester Number'),
        ),
    ]
