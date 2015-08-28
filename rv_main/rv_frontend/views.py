from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

import re

# Return a landing page if the user is not logged in, otherwise return the user to their map.
def index(request):
    if request.user.is_authenticated():
        return redirect('map')
    else:
        t = loader.get_template('index.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))

def map(request):
    if request.user.is_authenticated():
        t = loader.get_template('map.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c)) 

#### SIGN IN FUNCTIONS ####

# If the request is a post perform the login operation, otherwise serve the login page.
def login(request):
    
    if request.method == "POST":
    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            if user.is_active:
                auth_login(request, user)
                t = loader.get_template('index.html')
                c = RequestContext(request, {})
                return HttpResponse(t.render(c))
            else:
                t = loader.get_template('banned.html')
                c = RequestContext(request, {})
                return HttpResponse(t.render(c))
        else:

            t = loader.get_template('login_error.html')
            c = RequestContext(request, {})
            return HttpResponse(t.render(c))
    else:
        
        t = loader.get_template('login.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))

# If the request is a POST register a new user, otherwise serve the register page.
def register(request):
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        emailpattern = '[^@]+@[^@]+\.[^@]+'
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "Username already exists.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, "Email address already associated with account.")
            return redirect("register")
        if re.match(emailpattern, email) is None:
            messages.add_message(request, messages.ERROR, "Bro, do you even email?")
            return redirect("register")
    
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        return redirect("index")
                
    else:

        t = loader.get_template('register.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))
