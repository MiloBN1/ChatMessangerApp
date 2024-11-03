from django.contrib import admin
from django.urls import include, path
from main import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.get_users),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('auth.urls')),
    path('account/', include('account.urls')),
    path('hello/<str:name>/', views.get_hello, name='hello')
]
