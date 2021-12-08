from django.shortcuts import get_object_or_404
from project.models import Achievement


class AchievementDAL:
    @staticmethod
    def get_achievements_list():
        return Achievement.objects.all()

    @staticmethod
    def get_achievement_by_amount_to_reach(amount_to_reach):
        return get_object_or_404(Achievement, amount_to_reach=amount_to_reach)
