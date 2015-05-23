# -*- coding: utf-8 -*-
from django.db import models

class Masters(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)

class Services(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=50, decimal_places=10)
    description = models.CharField(max_length=500)

class ServicesOfMasters(models.Model):
    master = models.ForeignKey(Masters)
    service = models.ForeignKey(Services)

class Booking(models.Model):
    master = models.ForeignKey(Masters)
    service = models.ForeignKey(Services)
    date = models.DateField('date_published')
    time = models.TimeField('time_published')
