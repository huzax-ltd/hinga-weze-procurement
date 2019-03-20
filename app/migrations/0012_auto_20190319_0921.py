# Generated by Django 2.1.3 on 2019-03-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0011_auto_20190319_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('', '--select--'), ('pending', 'Pending'), ('requested', 'Requested'),
                                            ('level0-approved', 'Level0 Approved'),
                                            ('level1-approved', 'Level1 Approved'),
                                            ('level2-approved', 'Level2 Approved'),
                                            ('level3-approved', 'Level3 Approved'),
                                            ('level4-approved', 'Level4 Approved'),
                                            ('level1-rejected', 'Level1 Rejected'),
                                            ('level2-rejected', 'Level2 Rejected'),
                                            ('level3-rejected', 'Level3 Rejected'),
                                            ('level4-rejected', 'Level4 Rejected'), ('reviewed', 'Reviewed'),
                                            ('approved', 'Approved'), ('rejected', 'Rejected'),
                                            ('assigned', 'Assigned'), ('proposal-generated', 'Proposal Generated'),
                                            ('proposal-requested', 'Proposal Requested'),
                                            ('proposal-evaluated', 'Proposal Evaluated'),
                                            ('proposal-approved', 'Proposal Approved'),
                                            ('proposal-rejected', 'Proposal Rejected'),
                                            ('purchase-generated', 'Purchase Generated'),
                                            ('proposal-acknowledged', 'Proposal Acknowledged'),
                                            ('received', 'Received'), ('partially-paid', 'Partially Paid'),
                                            ('paid', 'Paid'), ('closed', 'Closed')], default='pending', max_length=255,
                                   verbose_name='Status'),
        ),
    ]