import json
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import User

@csrf_exempt  # Disable CSRF for this endpoint (for API-like behavior)
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the JSON body
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)

        User.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # Hash the password
        )
        
        return JsonResponse({'message': 'User created successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
