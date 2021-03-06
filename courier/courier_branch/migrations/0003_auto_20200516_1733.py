# Generated by Django 3.0.5 on 2020-05-16 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier_branch', '0002_auto_20200510_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='courier_name',
            field=models.CharField(help_text='Enter unique name of courier', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='sending_branch_name',
            field=models.ForeignKey(help_text='This Branch', on_delete=django.db.models.deletion.CASCADE, to='courier_branch.Branch'),
        ),
        migrations.AlterField(
            model_name='courierdetails',
            name='courier_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', help_text='Status of Courier', max_length=9),
        ),
    ]
