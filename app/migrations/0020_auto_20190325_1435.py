# Generated by Django 2.1.3 on 2019-03-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0019_auto_20190325_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_attachments',
            name='order_attachment_file_size',
            field=models.CharField(blank=True, max_length=255, verbose_name='File Size'),
        ),
        migrations.AddField(
            model_name='order_attachments',
            name='order_attachment_file_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='File Type'),
        ),
        migrations.AlterField(
            model_name='order_attachments',
            name='order_attachment_file_path',
            field=models.FileField(upload_to='orders/', verbose_name='File Path'),
        ),
        migrations.AlterField(
            model_name='order_attachments',
            name='order_attachment_type',
            field=models.CharField(
                choices=[('', '--select--'), ('order-email', 'Order Email'), ('order-proposal', 'Order Proposal'),
                         ('order-purchase', 'Order Purchase'), ('order-invoice', 'Order Invoice')], default='none',
                max_length=255, verbose_name='Type'),
        ),
    ]
