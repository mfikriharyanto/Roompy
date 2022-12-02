from rest_framework.decorators import api_view
from rest_framework.response import Response
from room.models import Room
from user.models import User
from .serializers import RoomSerializer

@api_view(['GET'])
def getRooms(request):
  rooms = Room.objects.all()
  serializer = RoomSerializer(rooms, many=True)
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