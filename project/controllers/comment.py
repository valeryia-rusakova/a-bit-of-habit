from rest_framework.exceptions import PermissionDenied

from project.dal.comment import CommentDAL
from project.dal.post import PostDAL


class CommentController:
    dal = CommentDAL()

    def get_comment_queryset(self, request, request_type):
        if request_type == 'list':
            return self.dal.get_comments_list()
        comment_pk = request.parser_context['kwargs']['pk']
        return self.dal.retrieve_comment(comment_pk)

    def create_comment(self, request):
        post_id = request.data['post']
        post_instance = PostDAL.retrieve_post(post_id)
        data = {
            'user': request.user,
            'body': request.data['body'],
            'post': post_instance,
        }
        return self.dal.insert_comment(data)

    def delete_comment(self, request):
        delete_pk = request.parser_context['kwargs']['pk']
        return self.dal.delete_comment(delete_pk)

    def update_comment(self, request):
        post_id = request.data['post']
        post_instance = PostDAL.retrieve_post(post_id)
        data = {
            'body': request.data['body'],
            'post': post_instance,
        }
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.update_comment(object_data=data, pk=update_pk)


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
