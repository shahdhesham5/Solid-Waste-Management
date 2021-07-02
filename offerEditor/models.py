from django.db import models
from django.conf import settings
# Create your models here.
class Offer(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='offers')
    companyName=models.CharField(max_length=255)
    companyAddress=models.CharField(max_length=255)
    keyContactName=models.CharField(max_length=255)
    companyNumber=models.CharField(max_length=16)
    solutionName=models.CharField(max_length=255)
    currentStage=models.CharField(max_length=25)
    clientQuery=models.CharField(max_length=400)
    lastMeetingDate=models.DateField()
    peojectDescribtion=models.CharField(max_length=400)
    clientQuery=models.CharField(max_length=400)

    def __str__(self):
        return self.companyName

class SubmittedForReview(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='submitted_offers')
    companyName=models.CharField(max_length=255)
    companyAddress=models.CharField(max_length=255)
    keyContactName=models.CharField(max_length=255)
    companyNumber=models.CharField(max_length=16)
    solutionName=models.CharField(max_length=255)
    currentStage=models.CharField(max_length=25)
    clientQuery=models.CharField(max_length=400)
    lastMeetingDate=models.DateField()
    peojectDescribtion=models.CharField(max_length=400)
    clientQuery=models.CharField(max_length=400)

    def __str__(self):
        return self.companyName


class Acceptedlist(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='accepted_offers')
    companyName=models.CharField(max_length=255)
    companyAddress=models.CharField(max_length=255)
    keyContactName=models.CharField(max_length=255)
    companyNumber=models.CharField(max_length=16)
    solutionName=models.CharField(max_length=255)
    currentStage=models.CharField(max_length=25)
    clientQuery=models.CharField(max_length=400)
    lastMeetingDate=models.DateField()
    peojectDescribtion=models.CharField(max_length=400)
    clientQuery=models.CharField(max_length=400)

    def __str__(self):
        return self.companyName
