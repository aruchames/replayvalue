from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

import re

# Create your views here.

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def login(request):
    
    if request.method == "POST":
    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print "FUK YES BITCCHES"
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
            print "oh no"
            t = loader.get_template('login_error.html')
            c = RequestContext(request, {})
            return HttpResponse(t.render(c))
    else:
        
        t = loader.get_template('login.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))

def register(request):
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        emailpattern = '[^@]+@[^@]+\.[^@]+'
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        
        if User.objects.filter(username=username).exists():
            print "username"
            messages.add_message(request, messages.ERROR, "Username already exists.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            print "email"
            messages.add_message(request, messages.ERROR, "Email address already associated with account.")
            return redirect("register")
        if re.match(emailpattern, email) is None:
            print "FUCK ME HARDER"
            messages.add_message(request, messages.ERROR, "Bro, do you even email?")
            return redirect("register")
    
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        return redirect("index")
                
    else:
        # yay
        t = loader.get_template('register.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))
