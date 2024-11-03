from django.http import HttpResponse, JsonResponse
from .models import User

def get_hello(request, name):
    return HttpResponse(f'Hello {name}!')

