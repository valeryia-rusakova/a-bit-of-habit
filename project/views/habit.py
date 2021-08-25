from project.controllers.habit import HabitController
from project.dal.habit import HabitDAL
from project.serializers import HabitSerializer
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from utils import has_permissions


class HabitView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    dal = HabitDAL()
    controller = HabitController()

    queryset = dal.get_habits_list()
    serializer_class = HabitSerializer

    @has_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_habit_queryset(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.create_habit(request)
        return Response(status=status.HTTP_201_CREATED)

    @has_permissions('anonymous')
    def retrieve(self, request, *args, **kwargs) -> Response:
        habit_object = self.controller.get_habit_queryset(request, 'retrieve')
        serializer = self.serializer_class(habit_object)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def destroy(self, request, *args, **kwargs) -> Response:
        self.controller.delete_habit(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @has_permissions('anonymous')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.update_habit(request)
        return Response(status=status.HTTP_200_OK)
