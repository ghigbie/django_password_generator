from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'generator/home.html', {'options': range(5, 20)})

def password(request):
    return render(request, 'generator/password.html')