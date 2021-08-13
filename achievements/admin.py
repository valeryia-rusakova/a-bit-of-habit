from django.contrib import admin

from achievements.models import AchievementUser, Achievement

admin.site.register(Achievement)
admin.site.register(AchievementUser)
