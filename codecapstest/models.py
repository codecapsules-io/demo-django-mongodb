from django.db import models
from djongo import models 

# Create your models here.

class testModel(models.Model):
    testField = models.CharField(max_length=50)
    testField2 = models.IntegerField()