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
