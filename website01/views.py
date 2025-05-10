#from django.http import HttpResponse
from django.shortcuts import render 

# import django.views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')