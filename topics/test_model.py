from django.test import TestCase
from .models import Topics, TopicsManager
from user.models import User
from room.models import Room

class TopicsTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(email='test@gmail.com', username='test', password='test')
        user2 = User.objects.create(email='test_followed@gmail.com', username='test_followed', password='test')

        topic1 = Topics.objects.create(name= 'topic1', topic_creator= user1)
        topic2 = Topics.objects.create(name= 'topic2', topic_creator= user1)

    def test_topic_creator(self):
        user = User.objects.get(username='test')
        topic = Topics.objects.get(name= 'topic1')

        self.assertEqual(topic.topic_creator, user)

    def test_default_total_followers(self):
        topic = Topics.objects.get(name= 'topic1')

        self.assertEqual(topic.total_followers,0)
    
    def test_add_follow_topic(self):
        user1 = User.objects.get(username='test')
        user2 = User.objects.get(username='test_followed')

        topic = Topics.objects.get(name= 'topic1')

        topic.add_follower(user1)
        topic.add_follower(user2)

        self.assertEqual(topic.total_followers,2)

        self.assertTrue(topic.topic_followers.filter(id = user1.id).exists())
        self.assertTrue(topic.topic_followers.filter(id = user2.id).exists())
    
    def test_remove_follow_topic(self):
        user1 = User.objects.get(username='test')
        user2 = User.objects.get(username='test_followed')

        topic = Topics.objects.get(name= 'topic1')

        ## pre follow and test
        topic.add_follower(user1)
        topic.add_follower(user2)
        self.assertEqual(topic.total_followers,2)
        self.assertTrue(topic.topic_followers.filter(id = user1.id).exists())
        self.assertTrue(topic.topic_followers.filter(id = user2.id).exists())

        ## remove test
        topic.remove_follower(user2)
        self.assertEqual(topic.total_followers,1)
        self.assertTrue(topic.topic_followers.filter(id = user1.id).exists())
        self.assertFalse(topic.topic_followers.filter(id = user2.id).exists())
    
    def test_follow_topic(self):
        user1 = User.objects.get(username='test')

        topic1 = Topics.objects.get(name= 'topic1')
        topic2 = Topics.objects.get(name= 'topic2')

        ## pre follow and test
        topic1.add_follower(user1)
        topic2.add_follower(user1)
        self.assertEqual(topic1.total_followers,1)
        self.assertEqual(topic2.total_followers,1)
        self.assertTrue(topic1.topic_followers.filter(id = user1.id).exists())
        self.assertTrue(topic2.topic_followers.filter(id = user1.id).exists())

        ## function test
        topics = TopicsManager.find_user_followed_topics(user1.username)
        self.assertTrue(topic1 in topics)
        self.assertTrue(topic2 in topics)