from django.contrib.gis.db import models

# Create your models here.
class Add(models.Model):
    name = models.CharField(max_length=255)


# class AddG(models.Model):
#     name = models.CharField(max_length=255)
#     point = models.PointField(srid=4326)


class Hs(models.Model):
    name= models.CharField(max_length=255)
    # po= models.MultiPolygonField(srid=4326)
    l = models.PointField(null=True)
    # point=models.PointField(srid=4326)
