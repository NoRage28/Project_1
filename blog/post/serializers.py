from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    post_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ['author_id', 'post_id']
