from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from room.models import Room, RoomManager
from topics.models import Topics, TopicsManager
from user.models import User
from topics.models import Topics
from .serializers import TopicsSerializer

@api_view(['GET'])
def getTopics(request):
  topics = Topics.objects.all()
  serializer = TopicsSerializer(topics, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getTopic(request, pk):
  topic = TopicsManager.get_topics(pk)

  if topic == None:
    return Response({'message': f'Topic with id {pk} does not exist'}, status=404)
  
  serializer = TopicsSerializer(topic, many=False)
  return Response(serializer.data)

@api_view(['GET'])
def getTrendingTopics(request):
  trending_topics = Topics.objects.all().order_by('-total_followers')[:10]
  serializer = TopicsSerializer(trending_topics, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def postFollowTopics(request, pk):
  if not request.user.is_authenticated:
    return Response(status=status.HTTP_403_FORBIDDEN)
  
  topics = Topics.objects.get(id=pk)
  user = User.objects.get(id=request.user.id)

  if not(topics.topic_followers.filter(id = user.id).exists()):
      topics.add_follower(user)
      topics.save()

      serializer = TopicsSerializer(topics, many=False)
      return Response(serializer.data)
  else:
    content = {'Bad Request': 'Youre already following the topic'}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postUnfollowTopics(request, pk):
  if not request.user.is_authenticated:
    return Response(status=status.HTTP_403_FORBIDDEN)
  
  topics = Topics.objects.get(id=pk)
  user = User.objects.get(id=request.user.id)

  if topics.topic_followers.filter(id = user.id).exists():
    topics.remove_follower(user)
    topics.save()

    serializer = TopicsSerializer(topics, many=False)
    return Response(serializer.data)
  else:
    content = {'Bad Request': 'Youre not following the topic'}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createTopics(request):
  if not request.user.is_authenticated:
    return Response(status=status.HTTP_403_FORBIDDEN)

  topic_name = request.data.get('topic')
  user = User.objects.get(id=request.user.id)

  try:
    topic = Topics.objects.get(name=topic_name)
    content = {'Bad Request': 'Topic already exist'}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)
  except Topics.DoesNotExist:
    topic = Topics.objects.create(
      name= topic_name,
      topic_creator= user,
    )

    serializer = TopicsSerializer(topic, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def followedTopics(request):
  if not request.user.is_authenticated:
    return Response(status=status.HTTP_403_FORBIDDEN)
    
  user = User.objects.get(id=request.user.id)

  topics = TopicsManager.find_user_followed_topics(user)

  serializer = TopicsSerializer(topics, many=True)
  return Response(serializer.data)