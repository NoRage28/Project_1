from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserSignUpTestCase(APITestCase):
    def test_signup_user(self):
        url = reverse('auth_register')
        data = {'username': 'third_user',
                'password': '1357246max',
                'password2': '1357246max'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'third_user')