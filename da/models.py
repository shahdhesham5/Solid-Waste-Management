from django.contrib.gis.db import models as gismodels
from django.db import models
from jsonfield import JSONField
# Create your models here.
class Hige(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()


class Higis(models.Model):
    name= models.CharField(max_length=255)
    po= gismodels.MultiPolygonField(srid=4326)

class editedLayers(models.Model):
    name=models.CharField(max_length=255)
    layer=JSONField()
    def __str__(self):
        return self.name
