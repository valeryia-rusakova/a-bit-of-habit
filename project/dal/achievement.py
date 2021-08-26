from django.shortcuts import get_object_or_404
from project.models import Achievement


class AchievementDAL:
    @staticmethod
    def retrieve_achievement(pk):
        return get_object_or_404(Achievement, pk=pk)

    @staticmethod
    def get_achievements_list():
        return Achievement.objects.all()

    @staticmethod
    def delete_achievement(pk):
        achievement = get_object_or_404(Achievement, pk=pk)
        achievement.delete()

    @staticmethod
    def insert_achievement(object_data: dict):
        Achievement.objects.create(**object_data)

    @staticmethod
    def update_achievement(object_data: dict, pk):
        achievement = get_object_or_404(Achievement, pk=pk)
        achievement.name = object_data['name']
        achievement.description = object_data['description']
        achievement.level = object_data['level']
        achievement.habit = object_data['habit']
        achievement.image = object_data['image']
        achievement.save()
