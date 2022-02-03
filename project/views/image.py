import base64
import json

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

    @staticmethod
    def export_svg_by_id(queryset, image_id):
        image_object = queryset.get(id=image_id)
        svg_bytes = image_object.image.file.file.read()
        data = ''.join(svg_bytes.decode("utf-8").split("\r\n"))
        return data

    @has_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_queryset(request, 'list')
        image_id_list = queryset.values_list('id', flat=True)
        serializer = self.serializer_class(queryset, many=True)
        data = serializer.data
        for image_id in image_id_list:
            svg_data = self.export_svg_by_id(queryset, image_id)
            data_item = next(item for item in data if item['id'] == image_id)
            data_item['image'] = svg_data
        return Response(data)

    @has_permissions('anonymous')
    def create(self, request, *args, **kwargs) -> Response:
        self.controller.create(request)
        return Response(status=status.HTTP_201_CREATED)

    @has_permissions('anonymous')
    def retrieve(self, request, *args, **kwargs) -> Response:
        image_object = self.controller.get_queryset(request, 'retrieve')
        serializer = self.serializer_class(image_object)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def destroy(self, request, *args, **kwargs) -> Response:
        self.controller.delete(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @has_permissions('anonymous')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.update(request)
        return Response(status=status.HTTP_200_OK)
