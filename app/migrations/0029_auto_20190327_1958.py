# Generated by Django 2.1.3 on 2019-03-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0028_auto_20190327_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_cancelled_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Cancelled At'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_cancelled_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Cancelled By'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_cancelled_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Cancelled Department'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_cancelled_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Cancelled ID'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_cancelled_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Cancelled Role'),
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
                                            ('proposal-acknowledged', 'Proposal Acknowledged'),
                                            ('received', 'Received'), ('partially-paid', 'Partially Paid'),
                                            ('paid', 'Paid'), ('closed', 'Closed'), ('cancelled', 'Cancelled')],
                                   default='pending', max_length=255, verbose_name='Status'),
        ),
    ]