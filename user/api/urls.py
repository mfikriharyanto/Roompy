from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_all_users),
  path('top-users', views.get_top_users),
  path('<str:pk>/follow', views.post_follow_user),
  path('<str:pk>/unfollow', views.post_unfollow_user),
  path('<str:pk>/flag-follow', views.check_follow),
]