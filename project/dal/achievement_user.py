from project.models import AchievementUser
from project.dal.MetaDAL import MetaDAL


class AchievementUserDAL(metaclass=MetaDAL):
    @staticmethod
    def get_user_achievements(user):
        return AchievementUser.objects.filter(user=user.id).select_related('achievement')

    @staticmethod
    def insert_user_achievement(object_data: dict):
        AchievementUser.objects.create(**object_data)
