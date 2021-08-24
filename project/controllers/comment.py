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
