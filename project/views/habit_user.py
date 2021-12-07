from rest_framework.response import Response
from rest_framework import mixins, viewsets, status

from project.controllers.habit_user import HabitUserController
from project.dal.habit import HabitDAL
from project.dal.habit_user import HabitUserDAL

from project.serializers import HabitSerializer
from utils import has_permissions


class HabitUserView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    dal = HabitDAL()
    controller = HabitUserController()
    serializer_class = HabitSerializer

    @has_permissions('user')
    def create(self, request, *args, **kwargs) -> Response:
        message = self.controller.create_habit_user(request)
        if message:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    @has_permissions('user')
    def list(self, request, *args, **kwargs) -> Response:
        user = request.user
        queryset = self.controller.get_habits_users(user)
        habit_id_list = queryset.values_list('habit', flat=True)
        habits = self.controller.get_filtered_habits_list(habit_id_list)
        serializer = self.serializer_class(habits, many=True)
        return Response(serializer.data)

    @has_permissions('user')
    def partial_update(self, request, *args, **kwargs) -> Response:
        message = self.controller.daily_check(request)
        if message:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
