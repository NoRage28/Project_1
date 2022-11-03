from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from freezegun import freeze_time
from users.models import UserActivity


@freeze_time('2022-11-01T00:00:00')
class UserActivityCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='TestUser', password='1357246max')

    def test_user_activity(self):
        auth_url = reverse('token_obtain_pair')
        self.access_token = self.client.post(auth_url, {
            'username': 'TestUser',
            'password': '1357246max'
        }).data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        post_create_url = reverse('post-list')
        data = {
            'title': 'title_text',
            'content': 'content_text'
        }
        self.client.post(post_create_url, data, format='json')
        url = reverse('activity-detail', kwargs=({'pk': self.user.id}))

        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{
            'user': UserActivity.objects.get().user.pk,
            'last_login': '2022-11-01T00:00:00',
            'last_request': '2022-11-01T00:00:00',

        }])
