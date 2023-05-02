# Generated by Django 4.2 on 2023-04-29 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('email', models.CharField(blank=True, default='', max_length=50)),
                ('age', models.IntegerField(blank=True, default=18)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.IntegerField(blank=True, default=10)),
            ],
        ),
    ]
