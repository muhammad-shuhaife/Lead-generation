from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Lead(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Mobile=models.IntegerField(blank=True,null=True)
    Source = models.CharField(max_length=30, null=True, blank=True)
    Password = models.CharField(max_length=30, null=True, blank=True)
    Confirmpassword = models.CharField(max_length=30, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

class contact(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Subject=models.CharField(max_length=30,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)

class Idcard(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Mobile=models.IntegerField(blank=True,null=True)
    Address = models.CharField(max_length=30, null=True, blank=True)
    Idnumber = models.CharField(max_length=30, null=True, blank=True)
    City = models.CharField(max_length=30, null=True, blank=True)
    Image = models.ImageField(blank=True, null=True)
    Sign = models.ImageField(blank=True, null=True)

class Candidate(models.Model):
    Name = models.CharField(max_length=100)
    Date=models.CharField(max_length=30,null=True,blank=True)
    Cvv=models.IntegerField(blank=True,null=True)
    Number=models.IntegerField(blank=True,null=True)
    start_date = models.DateField()
    emi_provider = models.CharField(max_length=100, blank=True)


