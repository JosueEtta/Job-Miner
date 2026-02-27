from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jobsignin/', views.jobsignin, name='jobsignin'),
    path('postsignin/', views.companysignin, name='postsignin'),
    path('login/', views.loginuser, name='login'),
    path('jobsearch/', views.jobSearch, name='jobsearch'),
    path('jobs/<int:job_id>/', views.jobDetails, name='jobdetail'),
    path('jobs/create/', views.createJob, name='createjob'),
    path('apply/<int:job_id>/', views.apply_job, name='applyjob'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('dashboard/jobseeker', views.jobseeker_dashboard, name='jobseeker_dashboard'),
    path('dashboard/jobs/more/', views.load_more_jobs, name='load_more_jobs'),
    path('dashboard/company', views.company_dashboard, name='company_dashboard'),
]