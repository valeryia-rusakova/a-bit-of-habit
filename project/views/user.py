from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project.controllers.user import UserController
from project.serializers import RegistrationSerializer, LoginSerializer
from utils import has_permissions


class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer
    user_controller = UserController()

    @has_permissions('anonymous')
    def post(self, request):
        try:
            user = request.data
            serializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"error": f"Error happened. Traceback: {e}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.user_controller.create_user(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    @has_permissions('anonymous')
    def post(self, request):
        try:
            user = request.data
        except Exception as e:
            return Response({"error": f"Error happened. Traceback: {e}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
