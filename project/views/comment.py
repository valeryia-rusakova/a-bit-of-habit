from project.controllers.comment import CommentController
from project.dal.comment import CommentDAL
from project.serializers import CommentSerializer
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from utils import has_permissions


class CommentView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    dal = CommentDAL()
    controller = CommentController()

    queryset = dal.get_comments_list()
    serializer_class = CommentSerializer

    @has_permissions('user')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_comment_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @has_permissions('user')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.create_comment(request)
        return Response(status=status.HTTP_201_CREATED)
