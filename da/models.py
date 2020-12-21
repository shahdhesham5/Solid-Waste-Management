from django.contrib.gis.db.models import PointField
from django.db import models
# Create your models here.
class Hige(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()


class Higis(models.Model):
    name= models.CharField(max_length=255)
    po= PointField()
