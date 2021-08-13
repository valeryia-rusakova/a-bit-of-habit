from django.db import models
from enums.habit_enum import HabitType
from dal.image_model import Image


class Habit(models.Model):

    name = models.CharField(verbose_name='habit name', unique=True, max_length=60)
    description = models.TextField(verbose_name='habit description')
    type = models.CharField(verbose_name='habit type', choices=HabitType.choices(), max_length=60)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'

    def __str__(self):
        return self.name



