from datetime import timedelta, datetime
import jwt
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password
from development import settings
from enums import AchievementLevel, HabitType


class Achievement(models.Model):
    name = models.CharField(verbose_name='achievement name', choices=AchievementLevel.choices(), max_length=80)
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
    user = models.ForeignKey("UserAccount", on_delete=models.CASCADE)
    description = models.TextField(verbose_name='achievement description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_username()


class Comment(models.Model):
    user = models.ForeignKey("UserAccount", on_delete=models.CASCADE)
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
    user = models.ForeignKey("UserAccount", null=True, on_delete=models.SET_NULL)
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
    header = models.CharField(verbose_name='post name', unique=True, max_length=80)
    body = models.TextField(verbose_name='post text', blank=False, null=False)
    user = models.ForeignKey("UserAccount", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.header


class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        password = make_password(password)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_username(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
