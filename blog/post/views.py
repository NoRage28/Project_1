from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from .models import Post, Like
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, id=pk)
        Like.objects.get_or_create(author=user, post=post)
        return Response("Like successfully added")

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, id=pk)
        Like.objects.filter(author=user, post=post).delete()
        return Response("Like successfully removed")

# class LikeViewSet(mixins.ListModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
