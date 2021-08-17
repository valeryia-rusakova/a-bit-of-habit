from rest_framework.exceptions import PermissionDenied

from project.dal.post import PostDAL


class PostController:
    dal = PostDAL()

    @staticmethod
    def _user_role_permissions(request):
        user = request.user
        if user.is_anonymous:
            return 'user_any'
        elif user.is_superuser:
            return 'user_admin'
        return 'user_authenticated'

    def _check_permissions(self, request, request_type: str) -> bool:
        permissions_list = {
            'list': ['user_any', 'user_authenticated', 'user_admin'],
            'retrieve': ['user_any', 'user_authenticated', 'user_admin'],
            'post': ['user_authenticated', 'user_admin'],
            'update': ['user_authenticated', 'user_admin']
        }
        user_role = self._user_role_permissions(request)
        have_access = user_role in permissions_list[request_type]
        return have_access

    def queryset_response(self, request, request_type):
        if not self._check_permissions(request, request_type):
            raise PermissionDenied()
        if request_type == 'list':
            return self.dal.post_list()
        post_pk = request.parser_context['kwargs']['pk']
        return self.dal.post_retrieve(post_pk)
