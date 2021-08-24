import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Comment, Post
from project.serializers import CommentSerializer


class CommentModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@gmail.com', 'qwerty15432')
        self.post = Post.objects.create(header="test_header_1", body="test_body_1", user=self.user)
        self.comment = Comment.objects.create(post=self.post, body="test_body_2", user=self.user)
        self.valid_payload = {
            "body": "test_body",
            "post": self.post.pk,
        }

    def test_get_list(self):
        response = self.client.get(reverse('comments_list'))
        comments = Comment.objects.all()
        serializer_data = CommentSerializer(comments, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_retrieve(self):
        response = self.client.get(reverse('comment_detail', kwargs={'pk': self.comment.pk}))
        single_comment = Comment.objects.get(pk=self.comment.pk)
        serializer_data = CommentSerializer(single_comment).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_valid_comment(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.post(
            reverse('comments_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_update_post(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.put(
            reverse('comment_detail', kwargs={'pk': self.comment.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(
            reverse('comment_detail', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

