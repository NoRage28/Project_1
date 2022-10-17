from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response

from .serializers import UserSignUpSerializer, UserActivitySerializer
from rest_framework import generics
from .models import UserActivity


class UserSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSignUpSerializer


class UserActivityViewSet(viewsets.ReadOnlyModelViewSet
                          ):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
