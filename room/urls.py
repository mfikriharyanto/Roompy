from django.urls import include, path
from . import views

app_name = 'room'

urlpatterns = [
    path('', views.get_rooms, name="get-rooms"),
    path('create-room', views.create_room, name="create-room"),
]