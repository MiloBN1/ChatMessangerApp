from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'chatserver_users'
