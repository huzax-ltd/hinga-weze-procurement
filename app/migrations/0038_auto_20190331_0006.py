# Generated by Django 2.1.3 on 2019-03-31 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0037_auto_20190330_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_invoice_approval_updated_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Approved At'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_approval_updated_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Approved By'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_approval_updated_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Approved Department'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_approval_updated_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Approved ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_approval_updated_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Approved Role'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_cop_approval_updated_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Approved At'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_cop_approval_updated_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Approved By'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_cop_approval_updated_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Approved Department'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_cop_approval_updated_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Approved ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_cop_approval_updated_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Approved Role'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_daf_approval_updated_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Approved At'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_daf_approval_updated_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Approved By'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_daf_approval_updated_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Approved Department'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_daf_approval_updated_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Approved ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_daf_approval_updated_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Approved Role'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_payment_voucher_uploaded_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Uploaded At'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_payment_voucher_uploaded_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Uploaded By'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_payment_voucher_uploaded_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Uploaded Department'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_payment_voucher_uploaded_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Uploaded ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_payment_voucher_uploaded_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Uploaded Role'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_reviewed_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Reviewed At'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_reviewed_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Reviewed By'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_reviewed_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Reviewed Department'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_reviewed_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Reviewed ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_reviewed_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Reviewed Role'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_uploaded_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Uploaded At'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_uploaded_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Uploaded By'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_uploaded_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Uploaded Department'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_uploaded_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Uploaded ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_invoice_uploaded_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Uploaded Role'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('', '--select--'), ('pending', 'Pending'), ('requested', 'Requested'),
                                            ('level0-approved', 'Level0 Approved'),
                                            ('level1-approved', 'Level1 Approved'),
                                            ('level2-approved', 'Level2 Approved'),
                                            ('level3-approved', 'Level3 Approved'),
                                            ('level4-approved', 'Level4 Approved'),
                                            ('level5-approved', 'Level5 Approved'),
                                            ('level6-approved', 'Level6 Approved'),
                                            ('level1-rejected', 'Level1 Rejected'),
                                            ('level2-rejected', 'Level2 Rejected'),
                                            ('level3-rejected', 'Level3 Rejected'),
                                            ('level4-rejected', 'Level4 Rejected'),
                                            ('level5-rejected', 'Level5 Rejected'),
                                            ('level6-rejected', 'Level6 Rejected'), ('reviewed', 'Reviewed'),
                                            ('approved', 'Approved'), ('rejected', 'Rejected'),
                                            ('assigned', 'Assigned'), ('supplier-updated', 'Supplier Updated'),
                                            ('proposal-generated', 'Proposal Generated'),
                                            ('proposal-requested', 'Proposal Requested'),
                                            ('proposal-selected', 'Proposal Selected'),
                                            ('purchase-generated', 'Purchase Generated'),
                                            ('acknowledged', 'Acknowledged'), ('received', 'Received'),
                                            ('invoice-uploaded', 'Invoice Uploaded'),
                                            ('invoice-reviewed', 'Invoice Reviewed'),
                                            ('invoice-payment-voucher-generated', 'Invoice Payment Voucher Generated'),
                                            ('invoice-approved', 'Invoice Approved'),
                                            ('invoice-rejected', 'Invoice Rejected'),
                                            ('invoice-daf-approved', 'Invoice Daf Approved'),
                                            ('invoice-daf-rejected', 'Invoice Daf Rejected'),
                                            ('invoice-cop-approved', 'Invoice Cop Approved'),
                                            ('invoice-cop-rejected', 'Invoice Cop Rejected'), ('paid', 'Paid'),
                                            ('closed', 'Closed'), ('cancelled', 'Cancelled')], default='pending',
                                   max_length=255, verbose_name='Status'),
        ),
    ]
