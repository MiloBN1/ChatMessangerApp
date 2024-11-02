from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def who_am_i(request):
    return JsonResponse({'message':"ii"})