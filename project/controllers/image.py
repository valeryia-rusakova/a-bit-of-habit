from project.controllers.controller import Controller
from project.dal.image import ImageDAL


class ImageController(Controller):
    dal = ImageDAL()

    def get_queryset(self, request, request_type):
        if request_type == 'list':
            return self.dal.get_images_list()
        image_pk = request.parser_context['kwargs']['pk']
        return self.dal.retrieve_image(image_pk)

    def create(self, request):
        data = {
            'image': request.data['image'],
        }
        return self.dal.insert_image(data)

    def delete(self, request):
        delete_pk = request.parser_context['kwargs']['pk']
        return self.dal.delete_image(delete_pk)

    def update(self, request):
        data = {
            'image': request.data['image'],
        }
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.update_image(object_data=data, pk=update_pk)
