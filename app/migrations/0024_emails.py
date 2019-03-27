# Generated by Django 2.1.3 on 2019-03-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0023_auto_20190326_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('email_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('email_from', models.CharField(max_length=255, verbose_name='From')),
                ('email_from_name', models.CharField(max_length=255, verbose_name='From Name')),
                ('email_to', models.CharField(max_length=255, verbose_name='To')),
                ('email_cc', models.CharField(max_length=255, verbose_name='Cc')),
                ('email_subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('email_message', models.TextField(verbose_name='Message')),
                ('email_created_at', models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Created At')),
                ('email_created_id', models.CharField(blank=True, max_length=100, verbose_name='Created ID')),
                ('email_created_by', models.CharField(blank=True, max_length=100, verbose_name='Created By')),
                ('email_created_department',
                 models.CharField(blank=True, max_length=255, verbose_name='Created Department')),
                ('email_created_role', models.CharField(blank=True, max_length=255, verbose_name='Created Role')),
                ('email_updated_at', models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Updated At')),
                ('email_updated_id', models.CharField(blank=True, max_length=100, verbose_name='Updated ID')),
                ('email_updated_by', models.CharField(blank=True, max_length=100, verbose_name='Updated By')),
                ('email_updated_department',
                 models.CharField(blank=True, max_length=255, verbose_name='Updated Department')),
                ('email_updated_role', models.CharField(blank=True, max_length=255, verbose_name='Updated Role')),
                ('email_sent_at', models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Sent At')),
                (
                'email_delivered_at', models.DateTimeField(default='0001-01-01 00:00:00', verbose_name='Delivered At')),
                ('email_status', models.CharField(
                    choices=[('', '--select--'), ('pending', 'Pending'), ('sent', 'Sent'), ('delivered', 'Delivered')],
                    default='pending', max_length=255, verbose_name='Status')),
            ],
        ),
    ]
