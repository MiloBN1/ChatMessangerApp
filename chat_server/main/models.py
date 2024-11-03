from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('moderator', 'Moderator'),
        # Add other roles if necessary
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    class Meta:
        db_table = 'chatserver_users'
        unique_together = ('username', 'email')

    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
