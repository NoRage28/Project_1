from django.shortcuts import render
from .serializers import BlogPostSerializer
from .models import BlogPost
from rest_framework import viewsets


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

