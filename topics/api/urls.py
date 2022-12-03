from django.urls import path
from . import views

urlpatterns = [
  path('', views.getTopics),
  path('trending-topics', views.getTrendingTopics),
  path('<str:pk>/follow', views.postFollowTopics),
  path('<str:pk>/unfollow', views.postUnfollowTopics),
  path('create-topics/', views.createTopics),
  path('<str:pk>/', views.getTopic),
  path('followed', views.followedTopics),
]