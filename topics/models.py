from django.db import models

from user.models import User, UserManager
# from room.models import Room, RoomManager

class Topics(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    topic_creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name='%(class)s_requests_created', null=True)
    topic_followers = models.ManyToManyField(User, related_name='%(class)s_requests_followers', blank=True)
    total_followers = models.IntegerField(default=0)

    def add_follower(self, user):
        self.topic_followers.add(user)
        self.total_followers += 1
        self.save()

    def remove_follower(self, user):
        self.topic_followers.remove(user)
        self.total_followers -= 1
        self.save()

    def __str__(self):
        return self.name

class TopicsManager():
    def get_topics(pk):
        try:
            topic = Topics.objects.get(id=pk)
            return topic
        except Topics.DoesNotExist:
            return None

    def find_all_topics():
        return Topics.objects.all()
    
    def find_user_followed_topics(user):
        user = User.objects.get(username= user)
        all_topics = TopicsManager.find_all_topics()
        followed_topics = []

        for topic in all_topics:
            if topic.topic_followers.filter(id = user.id).exists():
                followed_topics.append(topic)
            else:
                continue
        
        return followed_topics