from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ['post_id']


class LikeAnalyticsSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ['likes_count', 'created_at']
