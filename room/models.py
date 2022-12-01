from django.db import models
from user.models import User
from topics.models import Topics

class Room(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 200)
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    total_followers = models.IntegerField(default=0)
    total_upvote = models.IntegerField(default=0)
    total_downvote = models.IntegerField(default=0)
    room_topic = models.ForeignKey(Topics, on_delete= models.CASCADE, null=True)