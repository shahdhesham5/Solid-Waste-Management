from django.contrib.gis.db import models

# Create your models here.
class Add(models.Model):
    name = models.CharField(max_length=255)


class AddG(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField()  
