from project.controllers.image import ImageController
from project.dal.image import ImageDAL
from project.serializers import ImageSerializer
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from utils import has_permissions


class ImageView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    dal = ImageDAL()
    controller = ImageController()

    queryset = dal.get_images_list()
    serializer_class = ImageSerializer

    @has_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_image_queryset(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.create_image(request)
        return Response(status=status.HTTP_201_CREATED)

    @has_permissions('anonymous')
    def retrieve(self, request, *args, **kwargs) -> Response:
        image_object = self.controller.get_image_queryset(request, 'retrieve')
        serializer = self.serializer_class(image_object)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def destroy(self, request, *args, **kwargs) -> Response:
        self.controller.delete_image(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @has_permissions('anonymous')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.update_image(request)
        return Response(status=status.HTTP_200_OK)
