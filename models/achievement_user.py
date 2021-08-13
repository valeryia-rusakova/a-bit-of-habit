from django.contrib.auth.models import User
from django.db import models
from models.achievement import Achievement


class AchievementUser(models.Model):
    achievements = models.ManyToManyField(Achievement, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()
