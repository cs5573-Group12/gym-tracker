# Generated by Django 4.2 on 2023-04-29 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_expiredate_alter_memberentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expiredate',
            field=models.DateField(default=datetime.datetime(2024, 4, 28, 17, 23, 15, 166502)),
        ),
        migrations.AlterField(
            model_name='member',
            name='joindate',
            field=models.DateField(default=datetime.datetime(2023, 4, 29, 17, 23, 15, 166493)),
        ),
        migrations.AlterField(
            model_name='memberentry',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 29, 17, 23, 15, 166781)),
        ),
    ]
