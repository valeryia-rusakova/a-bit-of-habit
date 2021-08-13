from django.db import models
from enums.achievement_enum import AchievementLevel
from dal.habit_model import Habit
from dal.image_model import Image


class Achievement(models.Model):
    name = models.CharField(verbose_name='achievement name', unique=True, max_length=30)
    description = models.TextField(verbose_name='achievement description')
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
