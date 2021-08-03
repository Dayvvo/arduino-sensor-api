from django.db import models
from django.db.models.base import Model

# Create your models here.

class APIField(models.Model):
    temperature = models.DecimalField(decimal_places=10,max_digits=10)
    moisture_content = models.DecimalField(decimal_places=10,max_digits=10)
    humidity = models.DecimalField(decimal_places=10,max_digits=10)
    date_time = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)