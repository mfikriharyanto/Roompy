from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from room.models import Room, RoomManager
from user.models import User
from topics.models import Topics, TopicsManager
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
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def postFollowRoom(request, pk):
  room = Room.objects.get(id=pk)
  user = User.objects.get(id=request.user.id)

  if room not in user.following_room.all():
      room.total_followers = room.total_followers + 1
      room.save()

      user.following_room.add(room)
      user.save()

  serializer = RoomSerializer(room, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def createRoom(request):

  topic_name = request.POST.get('topic')

  # create topic if topic doesn't exists
  try:
    topic = Topics.objects.get(name=topic_name)
  except Topics.DoesNotExist:
    topic = Topics.objects.create(name= topic_name, topic_creator= request.user)

  room = Room.objects.create(
      creator=request.user,
      topic=topic,
      name=request.POST.get('name'),
      description=request.POST.get('description'),
  )

  serializer = RoomSerializer(room, many=False)
  return Response(serializer.data)

