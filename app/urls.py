from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jobsignin/', views.jobsignin, name='jobsignin'),
    path('postsignin/', views.companysignin, name='postsignin'),
    path('login/', views.loginuser, name='login'),

]