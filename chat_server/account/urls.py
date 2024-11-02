from django.urls import path
from .views import who_am_i
urlpatterns = [
    path('whoami/', who_am_i, name='whoami')
]
