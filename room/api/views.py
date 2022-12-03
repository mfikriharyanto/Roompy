from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from room.models import Room, Topic, RoomManager
from user.models import User
from .serializers import RoomSerializer

@api_view(['GET'])
def getRooms(request):
  rooms = Room.objects.all()
  serializer = RoomSerializer(rooms, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
  room = RoomManager.get_room(pk)

  if room == None:
    return Response({'message': f'Room with id {pk} does not exist'}, status=404)
  
  serializer = RoomSerializer(room, many=False)
  return Response(serializer.data)

@api_view(['GET'])
def getTrendingRooms(request):
  trending_rooms = Room.objects.all().order_by('-total_followers')[:10]
  serializer = RoomSerializer(trending_rooms, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def postFollowRoom(request, pk):
  room = Room.objects.get(id=pk)
  user = User.objects.get(id=request.data.get('user_id'))

  if room not in user.following_room.all():
      room.total_followers = room.total_followers + 1
      room.save()

      user.following_room.add(room)
      user.save()

  serializer = RoomSerializer(room, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def createRoom(request):

  print("REQUEST: ")
  print(request.user)

  topic_name = request.data.get('topic')

  # create topic if topic doesn't exists
  topic, created = Topic.objects.get_or_create(name=topic_name)

  room = Room.objects.create(
      creator=request.user,
      topic=topic,
      name=request.data.get('name'),
      description=request.data.get('description')
  )

  serializer = RoomSerializer(room, many=False)
  return Response(serializer.data)

