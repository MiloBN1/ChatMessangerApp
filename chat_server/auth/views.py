import json
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import User
from django.middleware.csrf import get_token

def json_response(data, status=200):
    return JsonResponse(data, status=status)

def parse_json(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None

def user_exists(username):
    return User.objects.filter(username=username).exists()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = parse_json(request)
        if data is None:
            return json_response({'error': 'Invalid JSON'}, status=400)

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if user_exists(username):
            return json_response({'error': 'User already exists'}, status=400)

        User.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # Hash the password
        )
        
        csrf_token = get_token(request)
        return json_response({'message': 'User created successfully', 'csrfToken': csrf_token}, status=201)

    return json_response({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = parse_json(request)
        if data is None:
            return json_response({'error': 'Invalid JSON'}, status=400)

        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return json_response({'error': 'Invalid credentials'}, status=401)

        if check_password(password, user.password):
            csrf_token = get_token(request)
            return json_response({'csrfToken': csrf_token}, status=200)
        else:
            return json_response({'error': 'Invalid credentials'}, status=401)

    return json_response({'error': 'Invalid request method'}, status=400)
