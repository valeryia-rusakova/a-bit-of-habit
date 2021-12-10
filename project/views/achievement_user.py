from project.controllers.achievement_user import AchievementUserController
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from project.dal.achievement_user import AchievementUserDAL
from project.serializers import AchievementUserSerializer
from utils import has_permissions


class AchievementUserView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    dal = AchievementUserDAL()
    controller = AchievementUserController()
    serializer_class = AchievementUserSerializer

    @has_permissions('user')
    def list(self, request, *args, **kwargs) -> Response:
        user = request.user
        queryset = self.controller.get_user_achievements(user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
