from django.contrib import admin

from habits.models import HabitUser, Habit

admin.site.register(Habit)
admin.site.register(HabitUser)
