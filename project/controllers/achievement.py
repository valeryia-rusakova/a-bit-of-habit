from project.dal.achievement import AchievementDAL
from project.dal.habit import HabitDAL
from project.dal.image import ImageDAL


class AchievementController:
    dal = AchievementDAL()

    def get_achievement_queryset(self, request, request_type):
        if request_type == 'list':
            return self.dal.get_achievements_list()
        achievement_pk = request.parser_context['kwargs']['pk']
        return self.dal.retrieve_achievement(achievement_pk)

    def create_achievement(self, request):
        data = AchievementController.get_request_data(request)
        return self.dal.insert_achievement(data)

    def delete_achievement(self, request):
        delete_pk = request.parser_context['kwargs']['pk']
        return self.dal.delete_achievement(delete_pk)

    def update_achievement(self, request):
        data = AchievementController.get_request_data(request)
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.update_achievement(object_data=data, pk=update_pk)

    @staticmethod
    def get_request_data(request):
        image_instance = ImageDAL.retrieve_image(request.data['image'])
        data = {
            'name': request.data['name'],
            'image': image_instance,
            'amount_ro_reach': request.data['amount_ro_reach']
        }
        return data
