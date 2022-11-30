from django.db import models
from user.models import User

class Room(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 200)
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    followers = models.ManyToManyField(User, related_name='room_follower')
    total_followers = models.IntegerField(default=0)
    total_upvote = models.IntegerField(default=0)
    total_downvote = models.IntegerField(default=0)