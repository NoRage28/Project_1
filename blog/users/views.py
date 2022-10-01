from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .serializers import UserSignUpSerializer
from rest_framework import generics


class UserSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSignUpSerializer
