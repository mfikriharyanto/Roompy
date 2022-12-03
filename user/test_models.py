from django.test import TestCase
from .models import User, UserManager

class UserTest(TestCase):
  def setUp(self):
    User.objects.create(email='test@gmail.com', username='test', password='test')
    User.objects.create(email='test_followed@gmail.com', username='test_followed', password='test')
    User.objects.create(email='test_following@gmail.com', username='test_following', password='test')

  def test_email_user(self):
    user = User.objects.get(username='test')
    self.assertEqual(user.email, 'test@gmail.com')

  def test_default_follower_and_following_user(self):
    followed_user = User.objects.get(username='test_followed')
    following_user = User.objects.get(username='test_following')

    self.assertEqual(followed_user.total_follower_user, 0)
    self.assertEqual(followed_user.total_following_user, 0)
    self.assertEqual(following_user.total_follower_user, 0)
    self.assertEqual(following_user.total_following_user, 0)

  def test_follow_user(self):
    followed_user = User.objects.get(username='test_followed')
    following_user = User.objects.get(username='test_following')

    followed_user.add_follower(following_user)
    following_user.add_following(followed_user)

    self.assertEqual(followed_user.total_follower_user, 1)
    self.assertEqual(following_user.total_following_user, 1)

    self.assertTrue(followed_user.follower_user.filter(id = following_user.id).exists())
    self.assertTrue(following_user.following_user.filter(id = followed_user.id).exists())

  def test_unfollow_user(self):
    followed_user = User.objects.get(username='test_followed')
    following_user = User.objects.get(username='test_following')

    prev_total_follower_user = followed_user.total_follower_user
    prev_total_following_user = following_user.total_following_user

    followed_user.remove_follower(following_user)
    following_user.remove_following(followed_user)

    self.assertEqual(prev_total_follower_user - followed_user.total_follower_user, 1)
    self.assertEqual(prev_total_following_user - following_user.total_following_user, 1)

    self.assertFalse(followed_user.follower_user.filter(id = following_user.id).exists())
    self.assertFalse(following_user.following_user.filter(id = followed_user.id).exists())

  def test_find_all_user(self):
    self.assertEqual(len(UserManager.find_all_user()), 3)

  def test_get_user_exist(self):
    self.assertIsNotNone(UserManager.get_user('1'))

  def test_get_user_not_exist(self):
    self.assertIsNone(UserManager.get_user('0'))

  def test_usermanager_follow_user(self):
    followed_user = User.objects.get(username='test_followed')
    following_user = User.objects.get(username='test_following')

    self.assertFalse(UserManager.is_user_follow(following_user, followed_user.id))

    UserManager.follow_user(following_user.id, followed_user.id)
    self.assertTrue(UserManager.is_user_follow(following_user, followed_user.id))

  def test_usermanager_unfollow_user(self):
    followed_user = User.objects.get(username='test_followed')
    following_user = User.objects.get(username='test_following')

    UserManager.follow_user(following_user.id, followed_user.id)
    self.assertTrue(UserManager.is_user_follow(following_user, followed_user.id))

    UserManager.unfollow_user(following_user.id, followed_user.id)
    self.assertFalse(UserManager.is_user_follow(following_user, followed_user.id))