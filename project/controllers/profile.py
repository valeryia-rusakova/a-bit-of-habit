from project.dal.image import ImageDAL
from project.dal.profile import ProfileDAL


class ProfileController:
    dal = ProfileDAL()

    def get_profile_queryset(self, request, request_type):
        if request_type == 'list':
            return self.dal.get_profiles_list()
        profile_pk = request.parser_context['kwargs']['pk']
        return self.dal.retrieve_profile(profile_pk)

    def update_profile(self, request):
        image_instance = ImageDAL.retrieve_image(request.data['image'])
        data = {
            'image': image_instance,
            'birth_date': request.data['birth_date'],
        }
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.update_profile(object_data=data, pk=update_pk)
