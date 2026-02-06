from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(models.Model):
  name = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=50)
  is_anonymous = models.BooleanField(default=False)
  is_authenticated = models.BooleanField(default=False)
  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["name","password","role"]
      

class jobseeker(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='jobseeker')
   jobseeker_name = models.CharField(max_length=250)
   experience = models.IntegerField()
   skills = models.JSONField()
   resume = models.FileField(upload_to="resume")

class company(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='company')
   about_company = models.CharField(max_length=250)