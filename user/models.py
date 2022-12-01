from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email = models.EmailField(unique=True)
	follower_user = models.ManyToManyField('self', blank=True, related_name='follower', symmetrical=False)
	following_user = models.ManyToManyField('self', blank=True, related_name='following', symmetrical=False)
	following_room = models.ManyToManyField(to='room.Room', blank=True)