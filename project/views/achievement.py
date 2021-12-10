from project.controllers.achievement import AchievementController
from project.dal.achievement import AchievementDAL
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from project.serializers import AchievementSerializer
from utils import has_permissions


class AchievementView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    dal = AchievementDAL()
    controller = AchievementController()

    queryset = dal.get_achievements_list()
    serializer_class = AchievementSerializer

    @has_permissions('user')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_achievement_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
