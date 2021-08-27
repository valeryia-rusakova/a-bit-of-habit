import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Achievement, Habit, Image
from project.serializers import AchievementSerializer


class AchievementModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@gmail.com', 'qwerty15432')
        self.image = Image.objects.create(image='test_image')
        self.first_achievement = Achievement.objects.create(name='WOODEN', amount_to_reach=30, image=self.image)
        self.second_achievement = Achievement.objects.create(name='SILVER', amount_to_reach=90, image=self.image)
        self.valid_payload = {
            'name': 'PLATINUM',
            'amount_to_reach': 150,
            'image': self.image.pk,
        }

    def test_get_list(self):
        response = self.client.get(reverse('achievements_list'))
        achievements = Achievement.objects.all()
        serializer_data = AchievementSerializer(achievements, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_retrieve(self):
        response = self.client.get(reverse('achievement_detail', kwargs={'pk': self.first_achievement.pk}))
        single_achievement = Achievement.objects.get(pk=self.first_achievement.pk)
        serializer_data = AchievementSerializer(single_achievement).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_valid_achievement(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.post(
            reverse('achievements_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_update_achievement(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.put(
            reverse('achievement_detail', kwargs={'pk': self.first_achievement.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_achievement(self):
        response = self.client.delete(
            reverse('achievement_detail', kwargs={'pk': self.second_achievement.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
