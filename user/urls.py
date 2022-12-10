from django.urls import path
from . import views

urlpatterns = [
  path('top-users', views.top_users),
  path('<str:pk>', views.get_user),
  path('<str:pk>/edit', views.edit_user),
]