from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'options': range(5, 20)})

def password(request):
    characters = list('abcdefghijklmnopqrs')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        uppercase = bool(request.GET.get('uppercase'))

    if request.GET.get('numbers'):
        numbers = bool(request.GET.get('numbers'))

    if request.GET.get()'special'):
        special = bool(request.GET.get('special'))
        
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})