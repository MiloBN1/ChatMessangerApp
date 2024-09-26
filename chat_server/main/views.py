from django.http import HttpResponse
from django.shortcuts import render


def getHello(request, name):
    return HttpResponse(f'Hello {name}!')
