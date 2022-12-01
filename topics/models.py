from django.db import models

from user.models import User

class Topics(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    topic_creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name='%(class)s_requests_created')
    topic_followers = models.ManyToManyField(User, related_name='%(class)s_requests_followers', blank=True)
    total_followers = models.IntegerField(default=0)