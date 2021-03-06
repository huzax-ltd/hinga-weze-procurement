# Generated by Django 2.1.3 on 2019-03-31 00:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0038_auto_20190331_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operators',
            name='operator_role',
            field=models.CharField(
                choices=[('', '--select--'), ('NONE', 'NONE'), ('COP', 'COP'), ('OPM', 'OPM'), ('Director', 'Director'),
                         ('Adviser', 'Adviser'), ('Regional Manager', 'Regional Manager'),
                         ('District Manager', 'District Manager'), ('Field Officer', 'Field Officer'),
                         ('Procurement Officer', 'Procurement Officer'), ('HR Manager', 'HR Manager'),
                         ('Receptionist', 'Receptionist'), ('Stock Admin', 'Stock Admin'),
                         ('Accountant Manager', 'Accountant Manager'), ('Accountant Officer', 'Accountant Officer')],
                default='NONE', max_length=255, verbose_name='Role'),
        ),
    ]
