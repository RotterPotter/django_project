from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm, Author_Form, Quote_Form, Reset_Form
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .models import Author, Quote
from django.contrib.auth.decorators import login_required


def home(request):
    quotes = list()
    try:
        quote_objects = Quote.objects.all()

        for quote in quote_objects:
            quotes.append({'author': quote.author, 'text': quote.text})
    except:
        return render(request, 'index.html', {'quotes': quotes})
    
    return render(request, 'index.html', {'quotes': quotes})

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'sign_up.html', {'form': form})
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'You have'\
                             'signed up successfull')
            
            username = request.POST['username']
            password = request.POST['password1']
            # email = request.POST['email']
            user = authenticate(username=username, password=password)

            login(request, user)
            return HttpResponseRedirect('/')
        
        else:
            return render(request, 'sign_up.html', {'form': form})

def sing_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        print(user)
        
    
    return render(request, 'login.html', {'form': LoginForm()})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def authors(request, author_name=None):
    if not author_name is None:
        author = Author.objects.filter(name=author_name)
        return render(request, 'authors.html', {'authors': author})

    authors = list()
    print(author_name)

    for author in Author.objects.all():
        authors.append(author)

    return render(request, 'authors.html', {'authors': authors})

@login_required(login_url='/login/')
def new_author(request):
    if request.method == 'POST':
        form = Author_Form(request.POST)
        form.save()
        return HttpResponseRedirect('/authors/')


    return render(request, 'new_author.html', {'form': Author_Form()})

@login_required(login_url='/login/')
def new_quote(request):
    if request.method == 'POST':
        form = Quote_Form(request.POST)
        form.save()
        return HttpResponseRedirect('/')


    return render(request, 'new_quote.html', {'form': Quote_Form()})

def reset_password(request):
    if request.method == 'GET':
        return render(request, 'sign_up.html', {'form': Reset_Form()})
    
    if request.method == 'POST':
        user_email = request.POST['email']
        send_reset_email(user_email)
        return HttpResponseRedirect('/login/')

def send_reset_email(email:str):
    pass