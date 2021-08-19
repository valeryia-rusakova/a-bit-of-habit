from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from project.controllers.post import PostController, route_permissions
from project.dal.post import PostDAL
from project.serializers import PostSerializer


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

    queryset = dal.post_list()
    serializer_class = PostSerializer

    @route_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.queryset_response(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @route_permissions('anonymous')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.object_created_response(request)
        return Response(status=status.HTTP_201_CREATED)

    @route_permissions('anonymous')
    def retrieve(self, request, *args, **kwargs) -> Response:
        post_object = self.controller.queryset_response(request, 'retrieve')
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    @route_permissions('anonymous')
    def destroy(self, request, *args, **kwargs) -> Response:
        self.controller.object_delete_response(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @route_permissions('anonymous')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.object_update_response(request)
        return Response(status=status.HTTP_200_OK)
