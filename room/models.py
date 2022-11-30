from django.db import models
from user.models import User

class Room(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    total_upvote = models.IntegerField(default=0)
    total_downvote = models.IntegerField(default=0)