from project.models import Image


class ImageDAL:
    @staticmethod
    def retrieve_image(pk):
        return Image.objects.get(pk=pk)

    @staticmethod
    def get_images_list():
        return Image.objects.all()

    @staticmethod
    def delete_image(pk):
        print(pk)
        image = Image.objects.get(pk=pk)
        image.delete()

    @staticmethod
    def insert_image(object_data: dict):
        Image.objects.create(**object_data)

    @staticmethod
    def update_image(object_data: dict, pk):
        image = Image.objects.get(pk=pk)
        image.image = object_data['image']
        image.save()
