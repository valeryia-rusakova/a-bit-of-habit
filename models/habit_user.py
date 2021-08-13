from django.contrib.auth.models import User
from django.db import models
from models.habit import Habit
from enums.achievement_enum import AchievementLevel


class HabitUser(models.Model):
    habit = models.ForeignKey(Habit, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
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
