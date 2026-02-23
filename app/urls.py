from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jobsignin/', views.jobsignin, name='jobsignin'),
    path('postsignin/', views.companysignin, name='postsignin'),
    path('login/', views.loginuser, name='login'),
    path('jobsearch/', views.jobSearch, name='jobsearch'),
    path('jobs/<int:job_id>/', views.jobDetails, name='jobdetail'),
    path('jobseekerdashboard/', views.jobSeekerdashboard, name='jobseekerdashboard'),
    path('companydashboard/', views.companydashboard, name='companydashboard'),
    path('jobs/create/', views.createJob, name='createjob'),
]