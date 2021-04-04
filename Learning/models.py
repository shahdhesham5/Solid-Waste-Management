from django.db import models
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

from django.conf import settings




class Course(models.Model):
    name = models.CharField(max_length=255)
    cover =models.ImageField(null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('CourseDetail', kwargs={'pk': self.pk})


class Exam(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='exam')
    grade=models.IntegerField( )

    def __str__(self):
        return self.name.name


class Question(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='question')
    question=models.CharField(max_length=255)

    def __str__(self):
        return self.question
    class Meta:
        ordering =('id',)


class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    first_choice=models.CharField(max_length=255)
    second_choice=models.CharField(max_length=255)
    third_choice=models.CharField(max_length=255)
    fourth_choice=models.CharField(max_length=255)
    choices=[(first_choice,'first_choice'),(second_choice,'second_choice'),(third_choice,'third_choice'),(fourth_choice,'fourth_choice')]
    correct_answer=models.CharField(max_length=255)
    class Meta:
        ordering =('-id',)
    def __str__(self):
        return self.correct_answer



User = get_user_model()
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    Email =models.EmailField(max_length=255)
    courses=models.ManyToManyField(Course,related_name='students')


    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def get_absolute_url(self):
        return reverse('CourseDetail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.user.username


class Grade(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='grade')
    course =models.ForeignKey(Course,on_delete=models.CASCADE,related_name='grade')
    grade =models.IntegerField()
