from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def getHello(request):
    return HttpResponse('Hello Message')