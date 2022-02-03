from django.shortcuts import get_object_or_404
from project.models import Image
from project.dal.MetaDAL import MetaDAL


class ImageDAL(metaclass=MetaDAL):
    @staticmethod
    def retrieve_image(pk):
        return get_object_or_404(Image, pk=pk)

    @staticmethod
    def get_images_list():
        return Image.objects.all()

    @staticmethod
    def delete_image(pk):
        image = get_object_or_404(Image, pk=pk)
        image.delete()

    @staticmethod
    def insert_image(object_data: dict):
        Image.objects.create(**object_data)

    @staticmethod
    def update_image(object_data: dict, pk):
        image = get_object_or_404(Image, pk=pk)
        image.image = object_data['image']
        image.save()
