from rest_framework.decorators import api_view
from rest_framework.response import Response
from room.models import Room
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