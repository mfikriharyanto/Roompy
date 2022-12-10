from django.urls import path
from . import views

urlpatterns = [
  path('top-users', views.top_users),
]