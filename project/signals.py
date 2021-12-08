from django.db.models.signals import post_save
from django.dispatch import receiver

from project.dal.achievement import AchievementDAL
from project.dal.habit import HabitDAL
from project.models import HabitUser, AchievementUser


@receiver(post_save, sender=HabitUser)
def save_achievement_user(sender, instance, **kwargs):
    user = instance.user
    habit = HabitDAL.retrieve_habit(instance.habit_id)
    days_checked = instance.days_checked
    achievements = AchievementDAL.get_achievements_list()
    if days_checked in achievements.values_list('amount_to_reach', flat=True):
        achievement = AchievementDAL.get_achievement_by_amount_to_reach(days_checked)
        description = f"You’ve been keeping {habit.name} for {achievement.amount_to_reach} days"
        achievement_user = AchievementUser()
        achievement_user.user = user
        achievement_user.achievement = achievement
        achievement_user.description = description
        achievement_user.save()
