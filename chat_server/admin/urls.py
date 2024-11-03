from django.urls import path
from .views import RoleCheckView

urlpatterns = [
    path('role/check/', RoleCheckView.as_view(), name='role_check'),
]