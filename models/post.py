from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    header = models.CharField(verbose_name='post name', unique=True, max_length=30, blank=False, null=False)
    body = models.TextField(verbose_name='post text', blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.header
