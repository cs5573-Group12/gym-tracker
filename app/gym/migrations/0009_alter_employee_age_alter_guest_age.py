# Generated by Django 4.2 on 2023-04-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_remove_memberentry_member_delete_member_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(blank=True, default=18),
        ),
        migrations.AlterField(
            model_name='guest',
            name='age',
            field=models.IntegerField(blank=True, default=18),
        ),
    ]
