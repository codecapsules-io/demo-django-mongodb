from django.db import models
from djongo import models as djmodels

# Create your models here.


class testModel(djmodels.Model):
    id = djmodels.GenericObjectIdField(db_column="_id", primary_key=True)
    testField = djmodels.CharField(max_length=50)
    testField2 = djmodels.DecimalField(default=0, decimal_places=5, max_digits=20)