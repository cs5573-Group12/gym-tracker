# Generated by Django 4.2 on 2023-04-28 04:52

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_employee_gender_member_phone_alter_employee_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='startdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='guest',
            name='age',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='guestentry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='expiredate',
            field=models.DateField(default=datetime.datetime(2024, 4, 27, 4, 52, 15, 242270, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='joindate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='memberentry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
