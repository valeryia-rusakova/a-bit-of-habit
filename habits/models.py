from django.contrib.auth.models import User
from django.db import models

from enums.achievement_enum import AchievementLevel
from enums.habit_enum import HabitType
from images.models import Image


class Habit(models.Model):

    name = models.CharField(verbose_name='habit name', unique=True, max_length=60, blank=False, null=False)
    description = models.TextField(verbose_name='habit description', blank=False, null=False)
    type = models.CharField(verbose_name='habit type', choices=HabitType.choices(), max_length=60)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'

    def __str__(self):
        return self.name


class HabitUser(models.Model):

    habit = models.ForeignKey(Habit, null=True, blank=False, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    date_started = models.DateField(auto_created=True)
    is_checked = models.BooleanField(null=True)
    checked_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    achievement_level = models.CharField(
        verbose_name='habit level', choices=AchievementLevel.choices(), max_length=30, null=True, blank=True,
    )

    def __str__(self):
        return f"{self.user.get_username()}: {self.habit.name}" if self.habit else f"{self.user.get_username()}: " \
                                                                                     f"Blanks "
