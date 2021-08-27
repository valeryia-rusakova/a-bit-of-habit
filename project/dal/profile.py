from django.shortcuts import get_object_or_404
from project.models import Profile


class ProfileDAL:
    @staticmethod
    def retrieve_profile(pk):
        return get_object_or_404(Profile, pk=pk)

    @staticmethod
    def get_profiles_list():
        return Profile.objects.all()

    @staticmethod
    def update_profile(object_data: dict, pk):
        profile = get_object_or_404(Profile, pk=pk)
        profile.birth_date = object_data['birth_date']
        profile.image = object_data['image']
        profile.save()
