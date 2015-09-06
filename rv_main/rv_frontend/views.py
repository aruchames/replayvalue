from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from rv_backend.views import AddFriend, ApproveFriend, RemoveFriend
from rv_backend.models import Friendlist, FriendlistManager

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
    else:
        return redirect('login')
        
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
                return redirect(map)
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
        
        # Asssert validity of user
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
    
        #Create user
        user = User.objects.create_user(username, email, password)
        private = False
        
        #Create an associated Friendlist at user registration
        new_friendlist = Friendlist.objects.create_Friendlist(user, private)
        new_friendlist.save()
        
        #Log the user into the website
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        auth_login(request, user)
        return redirect("index")
                
    else:

        t = loader.get_template('register.html')
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))

def friends(request):
    
    if request.user.is_authenticated():
        t = loader.get_template('friends.html')
        c = RequestContext(request, {'pendingfriends_cnt':request.user.friendlist_set.get().pendingFriends.all().count(),
                                     'pending_friends':request.user.friendlist_set.get().pendingFriends.all(),
                                     'friends':request.user.friendlist_set.get().friends.all(),
                                     'friends_cnt':request.user.friendlist_set.get().friends.all().count()})
        return HttpResponse(t.render(c))
    else:
        return redirect('login')

def logout(request):
    auth_logout(request)
    return redirect('index')

def search(request):
    query = request.GET.get('q')
    if query:
        # There was a query entered.
        results = User.objects.filter(username=query)
        print results.count()
    else:
        # If no query was entered, simply return to same page
        return redirect('friends')
    return render(request, 'search_results.html', {'results': results})

def add_friend(request):
    friend = User.objects.get(username=request.path.split('/')[-1])
    user = User.objects.get(username=request.user.username)
    
    AddFriend(user, friend)
    
    return redirect(friends)

def friend_requests(request):

    if request.user.is_authenticated():
        t = loader.get_template('approve_friends.html')
        c = RequestContext(request, {'pendingfriends_cnt':request.user.friendlist_set.get().pendingFriends.all().count(),
                                     'pending_friends':request.user.friendlist_set.get().pendingFriends.all(),
                                     'friends':request.user.friendlist_set.get().friends.all(),
                                     'friends_cnt':request.user.friendlist_set.get().friends.all().count()})
        return HttpResponse(t.render(c))
    else:
        return redirect('login')

def approve_friend(request):
    
    requester = User.objects.get(username=request.path.split('/')[-1])
    approver = User.objects.get(username=request.user.username)
    
    ApproveFriend(approver, requester)
    
    return redirect(friends)

def remove_friend(request):
    
    deleted = User.objects.get(username=request.path.split('/')[-1])
    deleter = User.objects.get(username=request.user.username)

    RemoveFriend(deleter, deleted)
    
    return redirect(friends)
