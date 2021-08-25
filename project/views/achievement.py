from project.controllers.achievement import AchievementController
from project.dal.achievement import AchievementDAL
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from project.serializers import AchievementSerializer
from utils import has_permissions


class AchievementView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    dal = AchievementDAL()
    controller = AchievementController()

    queryset = dal.get_achievements_list()
    serializer_class = AchievementSerializer

    @has_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_achievement_queryset(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.create_achievement(request)
        return Response(status=status.HTTP_201_CREATED)

    @has_permissions('anonymous')
    def retrieve(self, request, *args, **kwargs) -> Response:
        achievement_object = self.controller.get_achievement_queryset(request, 'retrieve')
        serializer = self.serializer_class(achievement_object)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def destroy(self, request, *args, **kwargs) -> Response:
        self.controller.delete_achievement(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @has_permissions('anonymous')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.update_achievement(request)
        return Response(status=status.HTTP_200_OK)
