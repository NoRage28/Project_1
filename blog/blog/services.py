from post.models import Post, Like
from django.shortcuts import get_object_or_404


def like_post(user, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(author=user, post=post)


def unlike_post(user, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(author=user, post=post).delete()


