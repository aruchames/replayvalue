
from django.conf.urls import patterns, url
from .  import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^map$', views.map, name='map'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^friends$', views.friends, name='friends'),
]
