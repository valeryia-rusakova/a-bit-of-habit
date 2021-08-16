from django.contrib import admin
from project.models import Achievement, AchievementUser, Profile, Comment, Post, HabitUser, Habit, Image

admin.site.register(Achievement)
admin.site.register(AchievementUser)
admin.site.register(Habit)
admin.site.register(HabitUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Image)
