# Generated by Django 2.1.3 on 2019-03-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0036_auto_20190330_1901'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order_Attachments',
        ),
        migrations.AlterField(
            model_name='attachments',
            name='attachment_file_path',
            field=models.FileField(upload_to='unknown/', verbose_name='File Path'),
        ),
        migrations.AlterField(
            model_name='attachments',
            name='attachment_model',
            field=models.CharField(
                choices=[('', '--select--'), ('none', 'None'), ('emails', 'Emails'), ('orders', 'Orders')],
                default='none', max_length=255, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='attachments',
            name='attachment_type',
            field=models.CharField(
                choices=[('', '--select--'), ('none', 'None'), ('email', 'Email'), ('order', 'Order'),
                         ('order-email', 'Order Email'),
                         ('order-proposal-business-license', 'Order Proposal Business License'),
                         ('order-proposal-offer-letter', 'Order Proposal Offer Letter'),
                         ('order-proposal-quotation', 'Order Proposal Quotation'),
                         ('order-proposal-vat-registration', 'Order Proposal Vat Registration'),
                         ('order-proposal-other-document', 'Order Proposal Other Document'),
                         ('order-proposal-reference-document', 'Order Proposal Reference Document'),
                         ('order-purchase', 'Order Purchase'), ('order-invoice', 'Order Invoice')], default='none',
                max_length=255, verbose_name='Type'),
        ),
    ]
