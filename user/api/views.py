from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from .serializers import UserSerializer

@api_view(['GET'])
def getUsers(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def postFollowUser(request, pk):
  try:
    followerUser = User.objects.get(id = request.user.id)
    followingUser = User.objects.get(id = pk)

    if followerUser == followingUser:
      return Response({'message': 'You can\'t follow your own account'}, status=400)

    if followerUser.following_user.filter(id = pk).exists():
      return Response({'message': f'You\'ve followed {followingUser}'}, status=400)

    followerUser.following_user.add(followingUser)
    followingUser.follower_user.add(followerUser)
      
  except User.DoesNotExist:
    return Response({'message': f'User with id {pk} does not exist'}, status=404)

  return Response({'message': f'Success follow {followingUser}'}, status=200)