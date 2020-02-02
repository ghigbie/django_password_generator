from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'options': range(5, 20)})

def password(request):
    characters = list('abcdefghijklmnopqrs')
    length = 10
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})