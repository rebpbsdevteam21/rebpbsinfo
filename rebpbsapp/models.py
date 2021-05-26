from django.db import models
from django.contrib.auth.models import User

from .views import *

class NetMeterInfo(models.Model):
    install_meter_nos=models.IntegerField(blank=True, null=True)
    capacity_of_install_meter=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=50, blank=True, null=True)
    year=models.CharField(max_length=50, blank=True, null=True)
    fy=models.CharField(max_length=50, blank=True, null=True)
    pbs_code=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.month

class SolarPanelInfo(models.Model):
    last_month_solar_panel_consumer_nos=models.IntegerField(blank=True, null=True)
    last_month_solar_panel_capacity=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=50, blank=True, null=True)
    year=models.CharField(max_length=50, blank=True, null=True)
    fy=models.CharField(max_length=50, blank=True, null=True)
    pbs_code=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.month
class GridChargingStationInfo(models.Model):
    charging_station_nos=models.IntegerField(blank=True, null=True)
    charging_station_capacity=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=50, blank=True, null=True)
    year=models.CharField(max_length=50, blank=True, null=True)
    fy=models.CharField(max_length=50, blank=True, null=True, verbose_name='Financial Year')
    pbs_code=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.month



