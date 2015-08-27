from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def login_load(request):
    t = loader.get_template('login.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            t = loader.get_template('profile.html')
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


                           

