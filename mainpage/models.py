from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Project_Country(models.Model):
    project_country=models.CharField(max_length=255)

    def __str__(self):
        return self.project_country

class Group_Team(models.Model):
    group=models.OneToOneField(Group,on_delete=models.CASCADE,related_name='project_group')
    describtion=models.CharField(max_length=255)
    project_countries=models.ManyToManyField(Project_Country,related_name='project_groups')
    def __str__(self):
        return self.group.name



class Project(models.Model):
    name=models.CharField(max_length=255)
    project_location=models.ForeignKey(Project_Country,on_delete=models.CASCADE,related_name='projects')
    project_group=models.ForeignKey(Group_Team,on_delete=models.CASCADE,related_name='projects')
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
