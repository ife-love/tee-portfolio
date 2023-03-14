import re
from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'portfolio/index.html')

def index(request):
    return render(request, 'portfolio/home.html')

def completed(request):
    return render(request, 'portfolio/completed.html')

def active(request):
    return render(request, 'portfolio/active.html')

def projects(request):
    return render(request, 'portfolio/project.html')

def sample(request):
    return render(request, 'portfolio/sample.html')


