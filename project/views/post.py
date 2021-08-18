from rest_framework import mixins, viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from project.controllers.post import PostController, route_permissions
from project.serializers import PostSerializer


class PostView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer
    controller = PostController()

    @route_permissions('user_any')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.queryset_response(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @route_permissions('user_authenticated')
    def retrieve(self, request, *args, **kwargs) -> Response:
        post_object = self.controller.queryset_response(request, 'retrieve')
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
