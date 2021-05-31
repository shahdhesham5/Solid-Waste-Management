from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Project_Team(models.Model):
    group=models.CharField(max_length=250)
    describtion=models.CharField(max_length=400)
    users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='project_teams')

    def __str__(self):
        return self.group

class Project_Country(models.Model):
    Project_group=models.ForeignKey(Project_Team,on_delete=models.CASCADE,related_name='project_locations')
    location=models.CharField(max_length=255)

    def __str__(self):
        return self.location

class Project(models.Model):
    name=models.CharField(max_length=255)
    project_location=models.ForeignKey(Project_Country,on_delete=models.CASCADE,related_name='projects')
    project_code=models.CharField(max_length=255)
    project_url=models.URLField(max_length=255)
    project_cover=models.ImageField(null=True)


    def __str__(self):
        return self.name


class Project_task(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='Project_tasks')
    task=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)

    def __str__(self):
         return self.task
