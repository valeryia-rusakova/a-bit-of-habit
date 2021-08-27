from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from project.controllers.profile import ProfileController
from project.dal.profile import ProfileDAL
from project.serializers import ProfileSerializer
from utils import has_permissions


class ProfileView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    dal = ProfileDAL()
    controller = ProfileController()

    queryset = dal.get_profiles_list()
    serializer_class = ProfileSerializer

    @has_permissions('anonymous')
    def list(self, request, *args, **kwargs) -> Response:
        queryset = self.controller.get_profile_queryset(request, 'list')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def retrieve(self, request, *args, **kwargs) -> Response:
        profile_object = self.controller.get_profile_queryset(request, 'retrieve')
        serializer = self.serializer_class(profile_object)
        return Response(serializer.data)

    @has_permissions('anonymous')
    def update(self, request, *args, **kwargs) -> Response:
        self.controller.update_profile(request)
        return Response(status=status.HTTP_200_OK)
