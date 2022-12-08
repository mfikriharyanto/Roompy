from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from user.models import UserManager
from .serializers import UserSerializer

@api_view(['GET'])
def get_all_users(request):
  users = UserManager.find_all_user()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def post_follow_user(request, pk):
  following_user = UserManager.get_user(request.user.id)
  followed_user = UserManager.get_user(pk)

  if followed_user != None:
    if following_user == followed_user:
      return Response({'message': 'You can\'t follow your own account'}, status=400)

    if UserManager.is_user_follow(following_user, followed_user.id):
      return Response({'message': f'You\'ve followed {followed_user}'}, status=400)

    UserManager.follow_user(request.user.id, pk)
  else:
    return Response({'message': f'User with id {pk} does not exist'}, status=404)

  return Response({'message': f'Success follow {followed_user}'}, status=200)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def post_unfollow_user(request, pk):
  following_user = UserManager.get_user(request.user.id)
  followed_user = UserManager.get_user(pk)

  if followed_user != None:
    if following_user == followed_user:
      return Response({'message': 'You don\'t follow your own account'}, status=400)

    if not UserManager.is_user_follow(following_user, followed_user.id):
      return Response({'message': f'You haven\'t followed {followed_user}'}, status=400)

    UserManager.unfollow_user(request.user.id, pk)
  else:
    return Response({'message': f'User with id {pk} does not exist'}, status=404)

  return Response({'message': f'Success unfollow {followed_user}'}, status=200)

@api_view(['GET'])
def get_top_users(request):
  top_users = UserManager.get_top_users(10)
  serializer = UserSerializer(top_users, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def check_follow(request, pk):
  following_user = UserManager.get_user(request.user.id)
  followed_user = UserManager.get_user(pk)

  if following_user == None or followed_user == None:
    data = { "is_followed": False }
    return Response(data)

  flag_follow = UserManager.is_user_follow(following_user, followed_user.id)
  data = { "is_followed": flag_follow }
  return Response(data)