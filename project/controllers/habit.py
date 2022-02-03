from project.controllers.controller import Controller
from project.dal.habit import HabitDAL
from project.dal.image import ImageDAL


class HabitController(Controller):
    dal = HabitDAL()

    def get_queryset(self, request, request_type):
        if request_type == 'list':
            return self.dal.get_habits_list()
        habit_pk = request.parser_context['kwargs']['pk']
        return self.dal.retrieve_habit(habit_pk)

    def create(self, request):
        image_id = request.data['image']
        image_instance = ImageDAL.retrieve_image(image_id)
        data = {
            'name': request.data['name'],
            'description': request.data['description'],
            'type': request.data['type'],
            'image': image_instance,
        }
        return self.dal.insert_habit(data)

    def delete(self, request):
        delete_pk = request.parser_context['kwargs']['pk']
        return self.dal.delete_habit(delete_pk)

    def update(self, request):
        image_id = request.data['image']
        image_instance = ImageDAL.retrieve_image(image_id)
        data = {
            'name': request.data['name'],
            'description': request.data['description'],
            'type': request.data['type'],
            'image': image_instance,
        }
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.update_habit(object_data=data, pk=update_pk)
