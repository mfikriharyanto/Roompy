from django.urls import include, path
from . import views

app_name = 'room'

urlpatterns = [
    path('', views.get_rooms, name="get-rooms"),
    path('<str:pk>/', views.get_room, name="get-room"),
]