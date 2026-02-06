from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from app.models import jobseeker,user,company
from django.http import HttpResponse

# Create your views here.

def home(request):

   return render(request,"app/index.html")

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
      
      #check if user email exist
      if user.objects.filter(email__iexact=email,role="job seeker").exists():
         #if exist return User already exist
         return render(request,'app/jobsignup.html',{"question":"User already exist"})
      else:
       #check password
       if confirm_password  == password:
        new_user= user.objects.create(name=name,email=email,password=password,role="job seeker")
        new_user.save()
        jobseeker.objects.create(user=new_user,jobseeker_name=name,skills=skills,experience=experience,resume=resume)
        return redirect("home")
       else:
         return render(request,'app/jobsignup.html',{"question":"Passwords don't match"})
    return render(request, 'app/jobsignup.html')

def companysignin(request):
   if request.method == "POST":
      #get request input
      name = request.POST.get('name')
      useremail = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      about_company = request.POST.get("about-company")
      
      #check if user email exist
      if user.objects.filter(email__iexact=useremail,role="company").exists():
         #if exist return User already exist
         return render(request,'app/postsignup.html',{"question":"User already exist"})
      else:
       #check password
       if confirm_password  == password:
        new_user= user.objects.create(name=name,email=useremail,password=password,role="company")
        new_user.save()
        company.objects.create(user=new_user,about_company=about_company)
        return redirect("home")
       else:
         return render(request,'app/postsignup.html',{"question":"Passwords don't match"})
   
   return render(request,'app/postsignup.html')   

def loginuser(request):
   if request.method == "POST":
      useremail = request.POST.get("email")
      userpassword = request.POST.get("password")
      authuser = authenticate(request,email="digimark@gmail.com",password = "hi")
      print(authuser)
      if authuser is not None:
          login(request,authuser)
          return render(request,"app/index.html")
      else:
         return render(request,'app/login.html',{"errormessage":"Invalid credentials"})
   return render(request,'app/login.html')

       