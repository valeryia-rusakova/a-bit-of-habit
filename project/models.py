from django.db import models
from django.contrib.auth.models import User
from enums import AchievementLevel, HabitType


class Achievement(models.Model):
    name = models.CharField(verbose_name='achievement name', choices=AchievementLevel.choices(), max_length=30)
    amount_to_reach = models.IntegerField(default=30)
    image = models.ForeignKey("Image", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'achievement'
        verbose_name_plural = 'achievement'

    def __str__(self):
        return self.name


class AchievementUser(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='achievement description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    body = models.TextField(verbose_name='comment text')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.user.get_username()


class Habit(models.Model):
    name = models.CharField(verbose_name='habit name', unique=True, max_length=60)
    description = models.TextField(verbose_name='habit description')
    type = models.CharField(verbose_name='habit type', choices=HabitType.choices(), max_length=60)
    image = models.ForeignKey("Image", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'

    def __str__(self):
        return self.name


class HabitUser(models.Model):
    habit = models.ForeignKey(Habit, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField(auto_created=True)
    days_checked = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_username()}: {self.habit.name}" if self.habit else f"{self.user.get_username()}: " \
                                                                                   f"Blanks "


class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class Post(models.Model):
    header = models.CharField(verbose_name='post name', unique=True, max_length=30)
    body = models.TextField(verbose_name='post text', blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.header


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.get_username()
