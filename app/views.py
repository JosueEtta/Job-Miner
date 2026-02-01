from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from app.models import jobseeker,user,company
from django.http import HttpResponse

# Create your views here.

def jobsignin(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      skills = request.POST.getlist('skills')
      skills = [s.strip().lower() for s in skills if s.strip()]
      experience = request.POST.get('experience')
      resume = request.FILES.get('resume')
      extension = resume.name
      extension = extension.split(".")[-1]
      if extension == "docx":
        resume.name = name+".docx"
      elif extension == "pdf":  
          resume.name = name+".pdf"    
      if confirm_password  == password:
       new_user= user.objects.create(name=name,email=email,password=password,role="job seeker")
       new_user.save()
      else:
         return render(request,'app/jobsignup.html',{"question":"Password and Confirm password don't match"})
      jobseeker.objects.create(user=new_user,jobseeker_name=name,skills=skills,experience=experience,resume=resume)
    return render(request, 'app/jobsignup.html')

def companysignin(request):
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      about_company = request.POST.get("about-company")
      if confirm_password  == password:
       new_user= user.objects.create(name=name,email=email,password=password,role="company")
       new_user.save()
      else:
         return render(request,'app/postsignup.html',{"question":"Password and Confirm password don't match"})
      company.objects.create(user=new_user,about_company=about_company)
   
   return render(request,'app/postsignup.html')   

def login(request):
   return render(request,'app/login.html')

       