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

@login_required(login_url='login')
def create_room(request):
    print("yeahh")
    
    topic_name = request.POST.get('topic')

        # create topic if topic doesn't exists
    try:
        topic = Topics.objects.get(name=topic_name)
    except Topics.DoesNotExist:
        topic = Topics.objects.create(name= topic_name, topic_creator= request.user)

    Room.objects.create(
        host=request.user,
        topic=topic,
        name=request.POST.get('name'),
        description=request.POST.get('description'),
    )
    return redirect('/')

def getRoom(request, pk):
  room = RoomManager.get_room(pk)