# Generated by Django 2.1.3 on 2019-03-12 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operators',
            name='operator_department',
            field=models.CharField(choices=[('', '--select--'), ('DCOP', 'Deputy COP'), ('BFM', 'Business, Finance & Marketing'), ('NUTRITION', 'Nutrition'), ('DAF', 'Administrative and Finance'), ('MAE', 'Monitoring and Evaluation'), ('GRANT-MANAGER', 'Grant Manager')], default='NONE', max_length=255, verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='operators',
            name='operator_parent_id',
            field=models.IntegerField(default='0', verbose_name='Parent Id'),
        ),
        migrations.AddField(
            model_name='operators',
            name='operator_role',
            field=models.CharField(choices=[('', '--select--'), ('COP', 'COP'), ('OPM', 'OPM'), ('Director', 'Director'), ('Adviser', 'Adviser'), ('Regional Manager', 'Regional Manager'), ('District Manager', 'District Manager'), ('Field Officer', 'Field Officer'), ('Procurement Officer', 'Procurement Officer'), ('HR Manager', 'HR Manager'), ('Stock Admin', 'Stock Admin'), ('Accountant Manager', 'Accountant Manager'), ('Accountant Officer', 'Accountant Officer')], default='NONE', max_length=255, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='operators',
            name='operator_type',
            field=models.CharField(choices=[('', '--select--'), ('super-admin', 'Super Admin'), ('admin', 'Admin'), ('manager', 'Manager'), ('other', 'Other')], default='other', max_length=20, verbose_name='Type'),
        ),
    ]
