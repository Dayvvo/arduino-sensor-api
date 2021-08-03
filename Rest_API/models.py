from django.db import models
from django.db.models.base import Model

# Create your models here.

class APIField(models.Model):
    temperature = models.FloatField()
    moisture_content = models.FloatField()
    humidity = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    country = models.CharField(max_length=40,null=True,blank=True)
    state = models.CharField(max_length=40,null=True,blank=True)
    city = models.CharField(max_length=40,null=True,blank=True)