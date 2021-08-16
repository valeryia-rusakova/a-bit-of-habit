from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enums import AchievementLevel, HabitType


class Achievement(models.Model):
    name = models.CharField(verbose_name='achievement name', unique=True, max_length=30)
    description = models.TextField(verbose_name='achievement description')
    level = models.CharField(verbose_name='achievement level', choices=AchievementLevel.choices(), max_length=30)
    habit = models.ForeignKey("Habit", null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ForeignKey("Image", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'achievement'
        verbose_name_plural = 'achievement'

    def __str__(self):
        return self.name


class AchievementUser(models.Model):
    achievements = models.ManyToManyField(Achievement, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    body = models.TextField(verbose_name='post text')
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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
