import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect,get_object_or_404
from app.models import jobseeker,user,company
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from .models import job,application
# Create your views here.

def home(request):
   jobs = job.objects.select_related('company', 'company__user')[:4]
   print(jobs)
   for field in jobs.model._meta.fields:
      print(field.name)
   data = [
            {
                'id':          j.pk,
                'title':       j.job_title,
                'company':     j.company.user.username,
                'type':        j.employment_type,
                'salaryMin':   j.min_salary,
                'salaryMax':   j.max_salary,
                'experience':  j.experience_required,
                'skills':      j.skills_required,
                'posted_date': j.posted_date.strftime('%Y-%m-%d'),
                'status':      'Active',
            }
            for j in jobs
        ]   
   return render(request,"app/index.html",{'jobs':data})

def jobsignin(request):
    if request.method == "POST":
      username = request.POST.get('name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      print("password",password)
      confirm_password = request.POST.get('confirm_password')
      print("Confirm password",confirm_password)
      skills = request.POST.getlist('skills')
      skills = [s.strip().lower() for s in skills if s.strip()]
      experience = request.POST.get('experience')
      resume = request.FILES.get('resume')
      extension = resume.name
      extension = extension.split(".")[-1]
      if extension == "docx":
        resume.name = username+".docx"
      elif extension == "pdf":  
          resume.name = username+".pdf"
      
      #check if user email exist
      if user.objects.filter(email__iexact=email,role="job seeker").exists():
         #if exist return User already exist
         return render(request,'app/jobsignup.html',{"errormessage":"User already exist"})
      else:
       #check password
       if confirm_password  == password:
        hashed_password = make_password(password)
        new_user= user.objects.create_user(username=username,email=email,password=password,role="job seeker")
        new_user.save()
        jobseeker.objects.create(user=new_user,jobseeker_name=username,skills=skills,experience=experience,resume=resume)
        return redirect("login")
       else:
         return render(request,'app/jobsignup.html',{"errormessage":"Passwords don't match"})
    return render(request, 'app/jobsignup.html')

def companysignin(request):
   if request.method == "POST":
      #get request input
      username = request.POST.get('name')
      useremail = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      about_company = request.POST.get("about-company")
      
      #check if user email exist
      if user.objects.filter(email__iexact=useremail,role="company").exists():
         #if exist return User already exist
         return render(request,'app/postsignup.html',{"errormessage":"User already exist"})
      else:
       #check password
       if confirm_password  == password:
      #   hashed_password = make_password(password)
        new_user= user.objects.create_user(username=username,email=useremail,password=password,role="company")
        new_user.save()
        company.objects.create(user=new_user,about_company=about_company)
        return redirect("login")
       else:
         return render(request,'app/postsignup.html',{"errormessage":"Passwords don't match"})
   
   return render(request,'app/postsignup.html')   

def loginuser(request):
   if request.method == "POST":
      user_email = request.POST.get("email")
      user_password = request.POST.get("password")
      print(user_email,user_password)
      authuser = authenticate(request,email=user_email,password=user_password)
      print(authuser)
      if authuser is not None:
          login(request,authuser)
          return redirect("home")
      else:
         return render(request,'app/login.html',{"errormessage":"Invalid credentials"})
   return render(request,'app/login.html')

def jobSearch(request):
    if request.headers.get('Accept') == 'application/json':
        
        jobs = job.objects.select_related('company', 'company__user').all()

        search     = request.GET.get('search', '')
        types      = request.GET.get('type', '')
        experiences = request.GET.get('experience', '')
        salary_min = request.GET.get('salary_min', '')
        salary_max = request.GET.get('salary_max', '')

        # ── Search by job title or company username ──
        if search:
            jobs = jobs.filter(
                Q(job_title__icontains=search) |
                Q(company__user__username__icontains=search)
            )

        # ── Filter by employment type ──
        if types:
            type_list = types.split(',')
            jobs = jobs.filter(employment_type__in=type_list)

        # ── Filter by experience ──
        if experiences:
            exp_map = {
                'Fresh':     (0, 0),
                '1-2 years': (1, 2),
                '3-5 years': (3, 5),
                '6-8 years': (6, 8),
                '9+ years':  (9, 99),
            }
            exp_q = Q()
            for exp in experiences.split(','):
                if exp in exp_map:
                    low, high = exp_map[exp]
                    exp_q |= Q(experience_required__gte=low, experience_required__lte=high)
            if exp_q:
                jobs = jobs.filter(exp_q)

        # ── Filter by salary ──
        if salary_min:
            jobs = jobs.filter(min_salary__gte=int(salary_min))
        if salary_max:
            jobs = jobs.filter(max_salary__lte=int(salary_max))

        data = [
            {
                'id':          j.pk,
                'title':       j.job_title,
                'company':     j.company.user.username,
                'type':        j.employment_type,
                'salaryMin':   j.min_salary,
                'salaryMax':   j.max_salary,
                'experience':  j.experience_required,
                'skills':      j.skills_required,
                'posted_date': j.posted_date.strftime('%Y-%m-%d'),
                'status':      'Active',
            }
            for j in jobs
        ]

        return JsonResponse({'jobs': data})

    return render(request, 'app/jobsearch.html')


def jobDetails(request, job_id):
    current_job = get_object_or_404(
        job.objects.select_related('company', 'company__user'),
        pk=job_id
    )

    similar_jobs = job.objects.select_related('company', 'company__user').filter(
        employment_type=current_job.employment_type
    ).exclude(pk=job_id)[:4]

    context = {
        'job': current_job,
        'similar_jobs': similar_jobs,
    }

    return render(request, 'app/jobdetail.html', context)

@require_POST
def createJob(request):
    try:
        data = json.loads(request.body)
        employer_company = company.objects.get(user=request.user)

        new_job = job.objects.create(
            company=employer_company,
            job_title=data.get('job_title'),
            responsibility=data.get('responsibility'),
            employment_type=data.get('employment_type'),
            min_salary=data.get('min_salary'),
            max_salary=data.get('max_salary'),
            experience_required=data.get('experience_required'),
            skills_required=data.get('skills_required'),
        )

        return JsonResponse({'success': True, 'job_id': new_job.pk})

    except company.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Company profile not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@login_required   
def dashboard_redirect(request):
   user = request.user

   if user.role == "job seeker":
      return redirect('jobseeker_dashboard')
   elif user.role == "company":
      return redirect('company_dashboard')
   else:
      return redirect('login')  

@login_required
def jobseeker_dashboard(request):   
    if request.user.role != "job seeker":
        return redirect("login")
    else:
        seeker = get_object_or_404(jobseeker, user=request.user)

    applications = application.objects.filter(
        jobseeker=seeker
    ).select_related('job', 'job__company', 'job__company__user')

    total        = applications.count()
    accepted     = applications.filter(status='accepted').count()
    pending      = applications.filter(status='pending').count()
    rejected     = applications.filter(status='rejected').count()
    success_rate = round((accepted / total * 100)) if total > 0 else 0

    # Exclude jobs already applied to
    applied_job_ids = applications.values_list('job_id', flat=True)
    available_jobs  = job.objects.select_related(
        'company', 'company__user'
    ).exclude(id__in=applied_job_ids)[:6]

    context = {
        'seeker':         seeker,
        'applications':   applications,
        'total':          total,
        'accepted':       accepted,
        'pending':        pending,
        'rejected':       rejected,
        'success_rate':   success_rate,
        'available_jobs': available_jobs,
    }

    return render(request, 'app/jobseekerdashboard.html', context)

@login_required
def load_more_jobs(request):
    offset = int(request.GET.get('offset', 0))
    limit  = 6

    try:
        seeker          = jobseeker.objects.get(user=request.user)
        applied_job_ids = application.objects.filter(
            jobseeker=seeker
        ).values_list('job_id', flat=True)
    except jobseeker.DoesNotExist:
        applied_job_ids = []

    jobs = job.objects.select_related(
        'company', 'company__user'
    ).exclude(id__in=applied_job_ids)[offset:offset + limit]

    total_available = job.objects.exclude(id__in=applied_job_ids).count()
    has_more        = (offset + limit) < total_available

    data = [
        {
            'id':              j.pk,
            'job_title':       j.job_title,
            'company':         j.company.user.username,
            'employment_type': j.employment_type,
            'min_salary':      j.min_salary,
            'max_salary':      j.max_salary,
            'posted_date':     j.posted_date.strftime('%Y-%m-%d'),
        }
        for j in jobs
    ]

    return JsonResponse({'jobs': data, 'has_more': has_more})

@login_required
def company_dashboard(request):
    if request.user.role != "company":
        return redirect("login")
    try:
        employer = company.objects.get(user=request.user)
    except company.DoesNotExist:
        return render(request, 'app/companydashboard.html', {
            'employer':        None,
            'active_jobs':     0,
            'total_applicants': 0,
            'total_jobs':      0,
            'applications':    [],
        })

    # All jobs posted by this company
    company_jobs = job.objects.filter(company=employer)

    # All applications for those jobs
    applications = application.objects.filter(
        job__in=company_jobs
    ).select_related(
        'jobseeker',
        'jobseeker__user',
        'job'
    )

    active_jobs      = company_jobs.count()
    total_applicants = applications.count()
    total_jobs       = company_jobs.count()

    context = {
        'employer':          employer,
        'active_jobs':       active_jobs,
        'total_applicants':  total_applicants,
        'total_jobs':        total_jobs,
        'applications':      applications,
    }

    return render(request, 'app/companydashboard.html', context)
 
@login_required
@require_POST
def apply_job(request, job_id):
    try:
        current_job = get_object_or_404(job, pk=job_id)
        seeker = get_object_or_404(jobseeker, user=request.user)

        # Check if already applied
        if application.objects.filter(job=current_job, jobseeker=seeker).exists():
            return JsonResponse({'status': 'error', 'message': 'You have already applied for this job'})

        application.objects.create(
            job=current_job,
            jobseeker=seeker,
        )

        return JsonResponse({'status': 'success', 'message': 'Application submitted successfully'})

    except jobseeker.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'You need a jobseeker profile to apply'}, status=403)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
   

        