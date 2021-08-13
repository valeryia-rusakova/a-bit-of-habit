from django.contrib.auth.models import User
from django.db import models

from enums.achievement_enum import AchievementLevel
from habits.models import Habit
from images.models import Image


class Achievement(models.Model):
    name = models.CharField(verbose_name='achievement name', unique=True, max_length=30, blank=False, null=False)
    description = models.TextField(verbose_name='achievement description', blank=False, null=False)
    level = models.CharField(verbose_name='achievement level', choices=AchievementLevel.choices(), max_length=30)
    habit = models.ForeignKey(Habit, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'achievement'
        verbose_name_plural = 'achievement'

    def __str__(self):
        return self.name


class AchievementUser(models.Model):
    achievements = models.ManyToManyField(Achievement, blank=True)
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()
