from django.http import HttpResponse, JsonResponse
from .models import User

def get_hello(request, name):
    return HttpResponse(f'Hello {name}!')


def get_users(request):
    # Fetch all user objects
    users = User.objects.all()
    
    # Prepare the user data to be serialized
    user_list = []
    for user in users:
        user_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            # Add more fields if necessary
        })
    
    return JsonResponse(user_list, safe=False)  # safe=False allows the response to be a list