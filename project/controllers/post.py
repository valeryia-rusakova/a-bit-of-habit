from rest_framework.exceptions import PermissionDenied
from project.dal.post import PostDAL
from rest_framework.request import Request


class PostController:
    dal = PostDAL()

    def queryset_response(self, request, request_type):
        if request_type == 'list':
            return self.dal.post_list()
        post_pk = request.parser_context['kwargs']['pk']
        return self.dal.post_retrieve(post_pk)

    def object_created_response(self, request):
        data = {
            'user': request.user,
            'header': request.POST.get('header'),
            'body': request.POST.get('body')
        }
        return self.dal.post_create(data)

    def object_delete_response(self, request):
        delete_pk = request.parser_context['kwargs']['pk']
        return self.dal.post_delete(delete_pk)

    def object_update_response(self, request):
        data = {
            'header': request.POST.get('header'),
            'body': request.POST.get('body'),
        }
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.post_update(object_data=data, pk=update_pk)



def route_permissions(permission):
    roles = {
        'admin': ['user_admin'],
        'user': ['user_admin', 'user_authenticated'],
        'anonymous': ['user_any', 'user_admin', 'user_authenticated'],
    }

    def decorator(view_method):
        def wrapper(self, *args, **kwargs):
            user = self.request.user
            if user.is_anonymous:
                user_role = 'user_any'
            elif user.is_superuser:
                user_role = 'user_admin'
            else:
                user_role = 'user_authenticated'
            if user_role in roles[permission]:
                return view_method(self, *args, **kwargs)
            else:
                raise PermissionDenied()

        return wrapper

    return decorator
