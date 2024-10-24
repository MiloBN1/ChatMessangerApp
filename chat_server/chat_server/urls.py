from django.contrib import admin
from django.urls import include, path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.get_users),
    path('auth/', include('auth.urls')),
    path('hello/<str:name>/', views.get_hello, name='hello')
]
