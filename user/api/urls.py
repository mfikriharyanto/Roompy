from django.urls import path
from . import views

urlpatterns = [
  path('', views.getUsers),
  path('<str:pk>/follow', views.postFollowUser),
]