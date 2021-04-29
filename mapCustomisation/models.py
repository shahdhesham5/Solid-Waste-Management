from django.contrib.gis.db import models as gismodels
from django.db import models
from jsonfield import JSONField
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Hige(models.Model):
    name= models.CharField(max_length=255)
    age= models.IntegerField()


class Higis(models.Model):
    name= models.CharField(max_length=255)
    po= gismodels.MultiPolygonField(srid=4326)




class Editor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='editor')

    company_Join_date=models.DateField(null=True, blank=True)
    class Meta:
        permissions=[('Edit_layers', 'Can edit layers')]
    def __str__(self):
        return "{}:{}".format(self.user.username,self.user.id)

class Superviser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='superviser')
    company_Join_date=models.DateField(null=True, blank=True)
    class Meta:
        permissions=[('Submit Edits', 'Can Review and sibmit  layers')]
    def __str__(self):
        return "{}:{}".format(self.user.username,self.user.id)



#

class editedLyr(models.Model):
    name=models.CharField(max_length=255)
    editor=models.ForeignKey(
        Editor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='edited_layers'
    )
    layer=JSONField()
    # def __str__(self):
    #     return self.name+' edited by '+self.editor



class AcceptedLyr(models.Model):
    name=models.CharField(max_length=255)
    editor=models.ForeignKey(
                Editor,
                on_delete=models.CASCADE,
                null=True,
                blank=True,
                related_name='accepted_layers'
            )
    superviser=models.ForeignKey(
                Superviser,
                on_delete=models.CASCADE,
                null=True,
                blank=True,
                related_name='accepted_layers'
            )
    layer=JSONField()
    # def __str__(self):
    #     return self.name+' Accepted by '+self.superviser

class RejectedLyr(models.Model):
        name=models.CharField(max_length=255)
        editor=models.ForeignKey(
                    Editor,
                    on_delete=models.CASCADE,
                    null=True,
                    blank=True,
                    related_name='rejected_layers'
                )
        superviser=models.ForeignKey(
                    Superviser,
                    on_delete=models.CASCADE,
                    null=True,
                    blank=True,
                    related_name='rejected_layers'
                )
        note=models.CharField(max_length=255)
        layer=JSONField()
        # def __str__(self):
        #     return self.name+' rejected by '+self.superviser +' to ' + self.user_name
