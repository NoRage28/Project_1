from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .serializers import PostSerializer, LikeSerializer, LikeAnalyticsSerializer
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_post(user=request.user, post_id=serializer.data['post_id'])
        return Response("Like successfully added")

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        unlike_post(user=request.user, post_id=serializer.data['post_id'])
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], serializer_class=LikeAnalyticsSerializer)
    def analytics(self, request):
        date_from = self.request.query_params['date_from']
        date_to = self.request.query_params['date_to']
        queryset = Like.objects.filter(created_at__gte=date_from, created_at__lte=date_to).values(
            'created_at').annotate(likes_count=Count('created_at'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LikeAnalyticsViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin):
    serializer_class = LikeAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        date_from = self.request.query_params['date_from']
        date_to = self.request.query_params['date_to']
        queryset = Like.objects.filter(created_at__gte=date_from, created_at__lte=date_to).values(
            'created_at').annotate(likes_count=Count('created_at'))
        serializer = LikeAnalyticsSerializer(queryset, many=True)
        return Response(serializer.data)
