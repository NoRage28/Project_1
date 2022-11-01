from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from post.models import Post, Like
from freezegun import freeze_time


class PostTestCase(APITestCase):
    @freeze_time('2022-10-27')
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='TestUser', password='1357246max')
        self.post = Post.objects.create(title='TestTitle', content='TestContent', author=self.user)
        self.like = Like.objects.create(author=self.user, post=self.post)
        self.client.force_authenticate(user=self.user)

    def test_post_create(self):
        url = reverse('post-list')
        data = {
            'title': 'title_text',
            'content': 'content_text'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.last().title, 'title_text')
        self.assertEqual(Post.objects.last().content, 'content_text')

    def test_like_create(self):
        post = Post.objects.create(author=self.user, title='post', content='content')
        url = reverse('post-like_create', kwargs={'pk': post.pk})
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.last().author, self.user)
        self.assertEqual(Like.objects.last().post, post)

    def test_like_remove(self):
        url = reverse('post-like_remove', kwargs={'pk': self.like.pk})
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.count(), 0)

    def test_like_analytics(self):
        url = reverse('like-like_analytics')
        data = {
            'date_from': '2022-10-25',
            'date_to': '2022-10-30'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(response.json(), [{'likes_count': 1, 'created_at': '2022-10-27'}])
