from django.http import HttpResponse

def hello_message(request):
    return HttpResponse("Hello, this is your message!")