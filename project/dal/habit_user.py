import datetime

from django.shortcuts import get_object_or_404

from project.models import HabitUser, Habit


class HabitUserDAL:
    @staticmethod
    def insert_habit_user(object_data: dict):
        HabitUser.objects.create(**object_data)

    @staticmethod
    def get_habits_users_list(user):
        return HabitUser.objects.filter(user=user.id)

    @staticmethod
    def get_habit_user(habit, user):
        return get_object_or_404(HabitUser, habit=habit, user=user.id)

    @staticmethod
    def get_filtered_habits_list(habits_id_list):
        return Habit.objects.filter(pk__in=habits_id_list)

    @staticmethod
    def daily_check(habit_user):
        habit_user.days_checked += 1
        habit_user.save(update_fields=['days_checked', 'updated_at'])
