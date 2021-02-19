from django.db import models

# Create your models here.
class WeatherModel(models.Model):
    region = models.CharField(max_length=50)
    req_date = models.DateTimeField(auto_now_add=True)
    temp_high = models.DecimalField(max_digits=3, decimal_places=1)
    temp_low = models.DecimalField(max_digits=3, decimal_places=1)
    rain_prob = models.DecimalField(max_digits=3, decimal_places=1)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.region + ',' + self.req_date

from django.db import models
from django.utils import timezone

# Create your models here.
class Todayweather(models.Model):
    location     = models.CharField(max_length=100)
    temp         = models.DecimalField(max_digits=3, decimal_places=1)
    feels_like   = models.DecimalField(max_digits=3, decimal_places=1)
    temp_min     = models.DecimalField(max_digits=3, decimal_places=1)
    temp_max     = models.DecimalField(max_digits=3, decimal_places=1)
    weather_desc = models.CharField(max_length=100)
    hmdt         = models.DecimalField(max_digits=3, decimal_places=1)
    wind_spd     = models.DecimalField(max_digits=3, decimal_places=2)
    date_time    = models.DateTimeField(auto_now_add=True)
    sunrise      = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    sunset       = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    pm2_5        = models.DecimalField(max_digits=3, decimal_places=2)
    pm10         = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
       return self.location