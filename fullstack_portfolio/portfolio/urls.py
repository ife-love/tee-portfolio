from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galaxy/', views.index, name='galaxy'),
    path('projects/completed/', views.completed, name='completed-projects'),
    path('projects/active/', views.active, name='active-projects'),
    path('projects/', views.projects, name='projects'),
    path('sample/', views.sample, name='sample'),
    ]