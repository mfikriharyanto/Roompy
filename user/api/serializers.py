from rest_framework.serializers import ModelSerializer
from user.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'about','total_follower_user', 'total_following_user']