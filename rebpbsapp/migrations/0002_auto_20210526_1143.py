# Generated by Django 3.2.3 on 2021-05-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rebpbsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridChargingStationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charging_station_nos', models.IntegerField(blank=True, null=True)),
                ('charging_station_capacity', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('fy', models.CharField(blank=True, max_length=50, null=True)),
                ('pbs_code', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolarPanelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_month_solar_panel_consumer_nos', models.IntegerField(blank=True, null=True)),
                ('last_month_solar_panel_capacity', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('fy', models.CharField(blank=True, max_length=50, null=True)),
                ('pbs_code', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='netmeterinfo',
            old_name='meter_nos',
            new_name='capacity_of_install_meter',
        ),
        migrations.RenameField(
            model_name='netmeterinfo',
            old_name='total_load',
            new_name='install_meter_nos',
        ),
        migrations.AddField(
            model_name='netmeterinfo',
            name='fy',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='netmeterinfo',
            name='pbs_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
