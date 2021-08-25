import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Image
from project.serializers import ImageSerializer


class ImageModelTest(APITestCase):
    def setUp(self):
        self.image1 = Image.objects.create(image='test_image1')
        self.image2 = Image.objects.create(image='test_image2')
        self.valid_payload = {
            "image": "test_image",
        }

    def test_get_list(self):
        response = self.client.get(reverse('images_list'))
        images = Image.objects.all()
        serializer_data = ImageSerializer(images, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_retrieve(self):
        response = self.client.get(reverse('image_detail', kwargs={'pk': self.image1.pk}))
        single_image = Image.objects.get(pk=self.image1.pk)
        serializer_data = ImageSerializer(single_image).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_valid_image(self):
        response = self.client.post(
            reverse('images_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_update_image(self):
        response = self.client.put(
            reverse('image_detail', kwargs={'pk': self.image1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_image(self):
        response = self.client.delete(
            reverse('image_detail', kwargs={'pk': self.image1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

