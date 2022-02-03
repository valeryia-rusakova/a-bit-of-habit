from django.shortcuts import get_object_or_404
from project.models import Habit
from project.dal.MetaDAL import MetaDAL


class HabitDAL(metaclass=MetaDAL):
    @staticmethod
    def retrieve_habit(pk):
        return get_object_or_404(Habit, pk=pk)

    @staticmethod
    def get_habits_list():
        return Habit.objects.all()

    @staticmethod
    def delete_habit(pk):
        habit = get_object_or_404(Habit, pk=pk)
        habit.delete()

    @staticmethod
    def insert_habit(object_data: dict):
        Habit.objects.create(**object_data)

    @staticmethod
    def update_habit(object_data: dict, pk):
        habit = get_object_or_404(Habit, pk=pk)
        habit.name = object_data['name']
        habit.description = object_data['description']
        habit.type = object_data['type']
        habit.image = object_data['image']
        habit.save()
