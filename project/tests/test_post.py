import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Post
from project.serializers import PostSerializer


class PostModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@gmail.com', 'qwerty15432')
        self.first_post = Post.objects.create(header="test_header_1", body="test_body_1", user=self.user)
        self.second_post = Post.objects.create(header="test_header_2", body="test_body_2", user=self.user)
        self.valid_payload = {
            "header": "test_header",
            "body": "test_body",
        }

    def test_get_list(self):
        response = self.client.get(reverse('posts_list'))
        posts = Post.objects.all()
        serializer_data = PostSerializer(posts, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_retrieve(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.first_post.pk}))
        single_post = Post.objects.get(pk=self.first_post.pk)
        serializer_data = PostSerializer(single_post).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_valid_post(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.post(
            reverse('posts_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_update_post(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.put(
            reverse('post_detail', kwargs={'pk': self.first_post.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(
            reverse('post_detail', kwargs={'pk': self.first_post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

