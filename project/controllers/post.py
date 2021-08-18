from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from project.dal.post import PostDAL


class PostController:
    dal = PostDAL()

    def queryset_response(self, request, request_type):
        if request_type == 'list':
            return self.dal.post_list()
        post_pk = request.parser_context['kwargs']['pk']
        return self.dal.post_retrieve(post_pk)


def route_permissions(permission):
    def decorator(view_method):
        def _decorator(self, *args, **kwargs):
            user = self.request.user
            if user.is_anonymous:
                user_role = 'user_any'
            elif user.is_superuser:
                user_role = 'user_admin'
            else:
                user_role = 'user_authenticated'
            if user_role == permission:
                return view_method(self, *args, **kwargs)
            else:
                raise PermissionDenied()

        return _decorator

    return decorator
