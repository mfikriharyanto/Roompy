from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from topics.models import Topics
from .forms import RoomForm
from room.models import Room, RoomManager

def get_rooms(request):
    form = RoomForm()
    topics = Topics.objects.all()
    context={
      'form': form,
      'topics': topics
    }
    return render(request, 'all_room.html', context)

def get_room(request, pk):
    room = RoomManager.get_room(pk)
    context={
    'room':room
    }
    return render(request, 'room.html', context)
    
def trending_rooms(request):
  return render(request, "trending_rooms.html")
