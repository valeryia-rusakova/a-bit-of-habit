from rest_framework import mixins, viewsets
from rest_framework.response import Response

from project.controllers.post import PostController
from project.serializers import PostSerializer


class PostView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PostSerializer
    controller = PostController()

    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.queryset_response(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs) -> Response:
        post_object = self.controller.queryset_response(request, 'retrieve')
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
