from django.db import models

# Create your models here.

class Sensor(models.Model):

    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    
