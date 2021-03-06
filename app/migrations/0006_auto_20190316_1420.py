# Generated by Django 2.1.3 on 2019-03-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0005_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_code',
            field=models.CharField(default=None, max_length=8, unique=True, verbose_name='Order Id'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_donor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Donor'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notification_from_id',
            field=models.IntegerField(default=0, verbose_name='From Id'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notification_to_id',
            field=models.IntegerField(default=0, verbose_name='To Id'),
        ),
        migrations.AlterField(
            model_name='order_logs',
            name='orders_order_id',
            field=models.IntegerField(default=0, verbose_name='Procurement Request Id'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Procurement Request Id'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_project_code',
            field=models.CharField(max_length=100, verbose_name='Project Code'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_requisition_number',
            field=models.CharField(max_length=100, verbose_name='Requester Number'),
        ),
    ]
