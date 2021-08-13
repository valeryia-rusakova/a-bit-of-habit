from django.db import models


class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
