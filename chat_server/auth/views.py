from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from main.models import User
import json

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
@require_http_methods(['POST'])
def register(request):
    data = parse_json(request)
    if data is None:
        return json_response({'error': 'Invalid JSON'}, status=400)

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if user_exists(username):
        return json_response({'error': 'User already exists'}, status=400)

    user = User.objects.create(
        username=username,
        email=email,
        password=make_password(password),
    )

    refresh = RefreshToken.for_user(user)
    return json_response({
        'message': 'User created successfully',
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }, status=201)

@csrf_exempt
@require_http_methods(['POST'])
def login(request):
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
        refresh = RefreshToken.for_user(user)
        return json_response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=200)
    else:
        return json_response({'error': 'Invalid credentials'}, status=401)
