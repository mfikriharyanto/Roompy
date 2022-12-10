from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_topic, name='create-topic'),
    path('all-topic/',views.all_topic, name='all-topic'),
    path('trending-topic/',views.trending_topic, name='trending-topic'),
]