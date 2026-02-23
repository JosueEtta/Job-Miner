from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(AbstractUser):
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=50)
  
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["username","role"]
      

class jobseeker(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='jobseeker')
   jobseeker_name = models.CharField(max_length=250)
   experience = models.IntegerField()
   skills = models.JSONField()
   resume = models.FileField(upload_to="resume")

class company(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='company')
   about_company = models.CharField(max_length=250)

class job(models.Model):
   company = models.ForeignKey(company,on_delete=models.CASCADE,related_name='company_jobs')
   job_title = models.CharField(max_length=250)
   responsibility = models.JSONField()
   employment_type = models.CharField(max_length=250)
   posted_date = models.DateField(auto_now_add=True)
   min_salary = models.IntegerField()
   max_salary = models.IntegerField()
   experience_required = models.IntegerField()
   skills_required = models.JSONField()
   
class application(models.Model):
   job = models.ForeignKey(job,on_delete=models.CASCADE,related_name='job_applications')
   jobseeker = models.ForeignKey(jobseeker,on_delete=models.CASCADE,related_name='jobseeker_applications')
   application_date = models.DateField(auto_now_add=True)
   status = models.CharField(max_length=50,default="pending")
