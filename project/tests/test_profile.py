import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Profile, Image
from project.serializers import ProfileSerializer


class ProfileModelTest(APITestCase):
    def setUp(self):
        self.first_user = User.objects.create_user('user_profile1', 'user1@gmail.com', 'qwerty15432')
        self.second_user = User.objects.create_user('user_profile2', 'user2@gmail.com', 'qwerty15432')
        self.image = Image.objects.create(image='test_image')
        self.valid_payload = {
            "birth_date": "2000-09-09",
            "image": self.image.pk,
        }

    def test_get_list(self):
        response = self.client.get(reverse('profiles_list'))
        profiles = Profile.objects.all()
        serializer_data = ProfileSerializer(profiles, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_retrieve(self):
        response = self.client.get(reverse('profile_detail', kwargs={'pk': self.first_user.pk}))
        single_profile = Profile.objects.get(pk=self.first_user.pk)
        serializer_data = ProfileSerializer(single_profile).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_valid_update_profile(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.put(
            reverse('profile_detail', kwargs={'pk': self.first_user.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
