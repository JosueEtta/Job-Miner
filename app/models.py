from django.db import models

# Create your models here.

class user(models.Model):
  name = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  role = models.CharField(max_length=50)
      

class jobseeker(models.Model):
   user = models.OneToOneField(user,on_delete=models.CASCADE,related_name='jobseeker')
   jobseeker_name = models.CharField(max_length=250)
   experience = models.IntegerField()
   skills = models.JSONField()
   resume = models.FileField(upload_to="resume")

class company(models.Model):
   user = models.OneToOneField(user, on_delete=models.CASCADE,related_name='company')
   about_company = models.CharField(max_length=250)