# Generated by Django 4.2 on 2023-04-28 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_remove_guest_expiredate_remove_guest_initialamount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='startdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 28, 4, 39, 4, 675783)),
        ),
        migrations.AlterField(
            model_name='guest',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='guest',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 28, 4, 39, 4, 676421)),
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='guestentry',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 28, 4, 39, 4, 676816)),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='expiredate',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 4, 27, 4, 39, 4, 676094)),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='joindate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 28, 4, 39, 4, 676086)),
        ),
        migrations.AlterField(
            model_name='member',
            name='plan',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='memberentry',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 28, 4, 39, 4, 676621)),
        ),
    ]
