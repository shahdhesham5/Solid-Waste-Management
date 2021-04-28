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

class editedLayer(models.Model):
    name=models.CharField(max_length=255)
    user_name=models.CharField(max_length=255)
    layer=JSONField()
    def __str__(self):
        return self.name+' edited by '+self.user_name



class AcceptedLayer(models.Model):
    name=models.CharField(max_length=255)
    user_name=models.CharField(max_length=255)
    superviser=models.CharField(max_length=255)
    layer=JSONField()
    def __str__(self):
        return self.name+' Accepted by '+self.superviser

class RejectedLayer(models.Model):
        name=models.CharField(max_length=255)
        user_name=models.CharField(max_length=255)
        superviser=models.CharField(max_length=255)
        note=models.CharField(max_length=255)
        layer=JSONField()
        def __str__(self):
            return self.name+' rejected by '+self.superviser +' to ' + self.user_name
