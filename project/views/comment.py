from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from project.controllers.comment import CommentController
from project.controllers.post import has_permissions
from project.dal.comment import CommentDAL
from project.serializers import CommentSerializer


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

    @has_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_comment_queryset(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.create_comment(request)
        return Response(status=status.HTTP_201_CREATED)

    @has_permissions('anonymous')
    def retrieve(self, request, *args, **kwargs) -> Response:
        comment_object = self.controller.get_comment_queryset(request, 'retrieve')
        serializer = self.serializer_class(comment_object)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def destroy(self, request, *args, **kwargs) -> Response:
        self.controller.delete_comment(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @has_permissions('anonymous')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.update_comment(request)
        return Response(status=status.HTTP_200_OK)
