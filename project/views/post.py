from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from project.controllers.post import PostController
from project.dal.post import PostDAL
from project.serializers import PostSerializer
from utils import has_permissions


class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    dal = PostDAL()
    controller = PostController()

    queryset = dal.get_posts_list()
    serializer_class = PostSerializer

    @has_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_queryset(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @has_permissions('user')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.create(request)
        return Response(status=status.HTTP_201_CREATED)

    @has_permissions('user')
    def retrieve(self, request, *args, **kwargs) -> Response:
        post_object = self.controller.get_queryset(request, 'retrieve')
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    @has_permissions('user')
    def destroy(self, request, *args, **kwargs) -> Response:
        self.controller.delete(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @has_permissions('user')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.update(request)
        return Response(status=status.HTTP_200_OK)

    @has_permissions('user')
    def get_extra_posts(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_extra_posts(request)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
