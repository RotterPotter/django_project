from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import LoginForm
from django.contrib import auth
from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

def registrate(request):
    

def login(request):
    pass

def logout(request):
    pass

def authors(request):
    return render(request, 'authors.html')