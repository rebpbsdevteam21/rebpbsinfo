# Generated by Django 3.2.3 on 2021-05-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetMeterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('meter_nos', models.IntegerField(blank=True, null=True)),
                ('total_load', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
