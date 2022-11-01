from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
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

    def retrieve(self, request, *args, **kwargs):
        instance = UserActivity.objects.filter(user_id=self.kwargs.get('pk'))
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)
