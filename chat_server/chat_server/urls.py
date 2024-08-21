from chat_server.views.hello_message import hello_message
from django.urls import path

urlpatterns = [
    path('hello/', hello_message, name='hello_message'),
]
