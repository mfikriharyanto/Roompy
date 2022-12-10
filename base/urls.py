from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
]