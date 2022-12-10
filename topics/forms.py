from django.forms import ModelForm
from .models import Topics

class TopicsForm(ModelForm):
    class Meta:
        model = Topics
        fields = ['name', 'topic_creator']