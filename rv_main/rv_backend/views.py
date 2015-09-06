from django.shortcuts import render
from django.http import HttpResponse

# For search algorithm
import re
from django.db.models import Q

import requests
from django.conf import settings

from rv_backend.models import Map, Friendlist, Game
from django.contrib.auth.models import User
#from rv_backend.serializers import FriendSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import generics

######################## Helper Functions   ###################################
def get_list(User):
    try:
        return Friendlist.objects.get(user = User).friends
    except Friendlist.DoesNotExist:
        raise Http404

def get_pendinglist(User):
    try:
        return Friendlist.objects.get(user=User).pendingFriends
    except Friendlist.DoesNotExist:
        raise Http404
###############################################################################

# Add a game to the map of a user, this method will contain much calculation

def AddFriend(User1, User2):
    list1 = get_pendinglist(User1)
    list2 = get_pendinglist(User2)
    list1.add(User2)
    list2.add(User1)
    Friendlist.objects.get(user=User1).save()
    Friendlist.objects.get(user=User2).save()
    print User1.username+ " wants to be friends with "+ User2.username
    print list1.all()
    print list2.all()

def ApproveFriend(User1, User2):
    list1 = get_pendinglist(User1)
    list2 = get_pendinglist(User2)
    list1.remove(User2)
    list2.remove(User1)
    
    list1 = get_list(User1)
    list2 = get_list(User2)
    list1.add(User2)
    list2.add(User1)

    Friendlist.objects.get(user=User1).save()
    Friendlist.objects.get(user=User2).save()
