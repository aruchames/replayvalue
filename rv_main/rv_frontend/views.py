from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))
