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
    topic = models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class RoomManager():
    def get_room(pk):
        try:
            room = Room.objects.get(id=pk)
            return room
        except Room.DoesNotExist:
            return None