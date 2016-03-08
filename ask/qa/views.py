#from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def test(request, *args, **kwargs):
    try:
        return HttpResponse('OK')
    except:
        raise Http404("Page not found")
# Create your views here.
