from django.conf.urls import patterns, url
from .  import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^map$', views.map, name='map'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^friends$', views.friends, name='friends'),
    url(r'^search_results$', views.search, name="search"),
    url(r'^add_friend/*', views.add_friend, name="addFriend"),
    url(r'^approve_friend/*', views.approve_friend, name="approveFriend"),
    url(r'^friend_requests$', views.friend_requests, name="friendRequests"),
    url(r'^remove_friend/*', views.remove_friend, name="removeFriend"),
    url(r'^friends/*', views.otherFriends, name="otherFriends"),
]
