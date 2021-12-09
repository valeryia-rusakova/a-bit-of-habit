from django.db.models.signals import post_save
from django.dispatch import receiver
from project.controllers.achievement_user import AchievementUserController
from project.dal.achievement import AchievementDAL
from project.models import HabitUser


@receiver(post_save, sender=HabitUser)
def save_achievement_user(sender, instance, **kwargs):
    days_checked = instance.days_checked
    achievements = AchievementDAL.get_achievements_list()
    if days_checked in achievements.values_list('amount_to_reach', flat=True):
        controller = AchievementUserController()
        controller.create_achievement_user(days_checked, instance.habit_id, instance.user)
