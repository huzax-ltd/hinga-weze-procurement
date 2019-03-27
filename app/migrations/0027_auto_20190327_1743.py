# Generated by Django 2.1.3 on 2019-03-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0026_auto_20190327_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_proposals',
            name='order_proposal_selected_at',
            field=models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Selected At'),
        ),
        migrations.AddField(
            model_name='order_proposals',
            name='order_proposal_selected_by',
            field=models.CharField(blank=True, max_length=100, verbose_name='Selected By'),
        ),
        migrations.AddField(
            model_name='order_proposals',
            name='order_proposal_selected_department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Selected Department'),
        ),
        migrations.AddField(
            model_name='order_proposals',
            name='order_proposal_selected_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Selected ID'),
        ),
        migrations.AddField(
            model_name='order_proposals',
            name='order_proposal_selected_role',
            field=models.CharField(blank=True, max_length=255, verbose_name='Selected Role'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notification_from_type',
            field=models.CharField(choices=[('', '--select--'), ('system', 'System'), ('order', 'Order'),
                                            ('order-proposal', 'Order Proposal'), ('supplier', 'Supplier'),
                                            ('operator', 'Operator')], default='system', max_length=20,
                                   verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notification_model_type',
            field=models.CharField(choices=[('', '--select--'), ('system', 'System'), ('order', 'Order'),
                                            ('order-proposal', 'Order Proposal'), ('supplier', 'Supplier'),
                                            ('operator', 'Operator')], default='system', max_length=20,
                                   verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notification_to_type',
            field=models.CharField(choices=[('', '--select--'), ('system', 'System'), ('order', 'Order'),
                                            ('order-proposal', 'Order Proposal'), ('supplier', 'Supplier'),
                                            ('operator', 'Operator')], default='system', max_length=20,
                                   verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='order_proposals',
            name='order_proposal_status',
            field=models.CharField(choices=[('', '--select--'), ('pending', 'Pending'), ('evaluated', 'Evaluated'),
                                            ('approved', 'Approved'), ('rejected', 'Rejected'),
                                            ('selected', 'Selected'), ('acknowledged', 'Acknowledged')],
                                   default='pending', max_length=255, verbose_name='Status'),
        ),
    ]
