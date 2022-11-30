from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def getUsers(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
  user = User.objects.get(id=pk)
  serializer = UserSerializer(user, many=False)
  return Response(serializer.data)