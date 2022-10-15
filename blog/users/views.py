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


class UserActivityViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet,
                          ):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = UserActivity.objects.filter(user_id=self.kwargs.get('pk'))
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)
