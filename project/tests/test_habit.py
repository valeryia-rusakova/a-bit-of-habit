import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Habit, Image
from project.serializers import HabitSerializer


class HabitModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@gmail.com', 'qwerty15432')
        self.image = Image.objects.create(image='test_image1')
        self.first_habit = Habit.objects.create(name='test_name1', description='test_description1',
                                                type='HEALTHY', image=self.image)
        self.second_habit = Habit.objects.create(name='test_name2', description='test_description1',
                                                 type='HEALTHY', image=self.image)
        self.valid_payload = {
            "name": "test_name",
            "description": "test_description",
            "type": "test_type",
            "image": self.image.pk,
        }

    def test_get_list(self):
        response = self.client.get(reverse('habits_list'))
        habits = Habit.objects.all()
        serializer_data = HabitSerializer(habits, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_retrieve(self):
        response = self.client.get(reverse('habit_detail', kwargs={'pk': self.first_habit.pk}))
        single_habit = Habit.objects.get(pk=self.first_habit.pk)
        serializer_data = HabitSerializer(single_habit).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_valid_habit(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.post(
            reverse('habits_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_update_habit(self):
        self.client.login(username='test_user', password='qwerty15432')
        response = self.client.put(
            reverse('habit_detail', kwargs={'pk': self.first_habit.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        response = self.client.delete(
            reverse('habit_detail', kwargs={'pk': self.first_habit.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
