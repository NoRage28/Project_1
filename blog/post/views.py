from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer, LikeSerializer
from .models import Post, Like
from rest_framework import viewsets, mixins
from blog.services import like_post, unlike_post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        like_post(user=request.user, post_id=pk)
        return Response("Like successfully added")

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk):
        unlike_post(user=request.user, post_id=pk)
        return Response("Like successfully removed")


class LikeViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_post(user=request.user, post_id=serializer.data['post_id'])
        return Response("Like successfully added")

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        unlike_post(user=request.user, post_id=serializer.data['post_id'])
        return Response("Like successfully removed")


