from rest_framework.exceptions import PermissionDenied
from project.dal.post import PostDAL


class PostController:
    dal = PostDAL()

    def get_post_queryset(self, request, request_type):
        if request_type == 'list':
            return self.dal.get_posts()
        post_pk = request.parser_context['kwargs']['pk']
        return self.dal.retrieve_post(post_pk)

    def create_post(self, request):
        data = {
            'user': request.user,
            'header': request.POST.get('header'),
            'body': request.POST.get('body')
        }
        return self.dal.insert_post(data)

    def delete_post(self, request):
        delete_pk = request.parser_context['kwargs']['pk']
        return self.dal.delete_post(delete_pk)

    def update_post(self, request):
        data = {
            'header': request.POST.get('header'),
            'body': request.POST.get('body'),
        }
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.update_post(object_data=data, pk=update_pk)


def has_permissions(permission):
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
