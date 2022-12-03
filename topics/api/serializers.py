from rest_framework.serializers import ModelSerializer
from topics.models import Topics

class TopicsSerializer(ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'