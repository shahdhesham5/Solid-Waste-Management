from django.contrib.gis.db import models
#from django.db import models
# Create your models here.
class Hige(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()


class Higis(models.Model):
    name= models.CharField(max_length=255)
    po= models.MultiPolygonField(srid=4326)
