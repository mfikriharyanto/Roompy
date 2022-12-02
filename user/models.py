from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email = models.EmailField(unique=True)
	follower_user = models.ManyToManyField('self', blank=True, related_name='follower_users', symmetrical=False)
	total_follower_user = models.IntegerField(default=0)
	following_user = models.ManyToManyField('self', blank=True, related_name='following_users', symmetrical=False)
	total_following_user = models.IntegerField(default=0)
	following_room = models.ManyToManyField(to='room.Room', blank=True)

	def add_following(self, user):
		self.following_user.add(user)
		self.total_following_user += 1
		self.save()

	def add_follower(self, user):
		self.follower_user.add(user)
		self.total_follower_user += 1
		self.save()

	def remove_following(self, user):
		self.following_user.remove(user)
		self.total_following_user -= 1
		self.save()

	def remove_follower(self, user):
		self.follower_user.remove(user)
		self.total_follower_user -= 1
		self.save()

class UserManager():
	def get_user(user_id):
		try:
			user = User.objects.get(id = user_id)
			return user
		except User.DoesNotExist:
			return None

	def find_all_user():
		return User.objects.all()

	def unfollow_user(following_user_id, followed_user_id):
		following_user = UserManager.get_user(following_user_id)
		followed_user = UserManager.get_user(followed_user_id)

		following_user.remove_following(followed_user)
		followed_user.remove_follower(following_user)

	def follow_user(following_user_id, followed_user_id):
		following_user = UserManager.get_user(following_user_id)
		followed_user = UserManager.get_user(followed_user_id)

		following_user.add_following(followed_user)
		followed_user.add_follower(following_user)

	def is_user_follow(following_user, followed_user_id):
		return following_user.following_user.filter(id = followed_user_id).exists()