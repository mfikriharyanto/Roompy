from django.urls import path
from . import views

urlpatterns = [
  path('', views.getRooms),
  path('trending-rooms', views.getTrendingRooms),
  path('<str:pk>/follow', views.postFollowRoom),
  path('create-room/', views.createRoom, name="create-room"),
  path('<str:pk>/', views.getRoom),
]