from django.db import models
from django.contrib import auth
from django.conf import settings



# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Rain(models.Model):
    date = models.DateField()
    rain_length = models.DecimalField(max_digits=20,decimal_places=10)

    def __unicode__(self):
        return '%s %s' % (self.date , self.rain_length)

class DamWaterYear(models.Model):
    month = models.CharField(max_length=10)
    mean_discharge= models.DecimalField(max_digits=20,decimal_places=10)

    def __unicode__(self):
        return '%s %s' % (self.month , self.mean_discharge)

class DamWaterDay(models.Model):
    Date = models.DateField()
    Discharge= models.DecimalField(max_digits=20,decimal_places=10)

    def __unicode__(self):
        return '%s %s' % (self.Date , self.Discharge)


class RoadSubmergenceDay(models.Model):
    date = models.DateField()
    date_discharge= models.DecimalField(max_digits=20,decimal_places=10)
    road_submergence = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s %s %s' % (self.date , self.date_discharge, self.road_submergence)

class RoadSubmergenceYear(models.Model):
    month = models.CharField(max_length=10)
    monthly_discharge= models.DecimalField(max_digits=20,decimal_places=10)
    rain_safe = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s %s %s' % (self.month , self.date_monthly_discharge, self.rain_safe)
