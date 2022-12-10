from django.urls import include, path
from . import views

urlpatterns = [
    path('trending-rooms', views.trending_rooms),
]