# Generated by Django 4.2 on 2023-04-29 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_member_registered_by_memberentry_checked_in_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expiredate',
            field=models.DateField(default=datetime.datetime(2024, 4, 28, 17, 20, 22, 882705, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='memberentry',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 29, 17, 20, 22, 883200)),
        ),
    ]
