from project.dal.comment import CommentDAL
from project.dal.post import PostDAL


class CommentController:
    dal = CommentDAL()

    def get_comment_queryset(self):
        return self.dal.get_comments_list()

    def create_comment(self, request):
        post_id = request.data['post']
        post_instance = PostDAL.retrieve_post(post_id)
        data = {
            'user': request.user,
            'body': request.data['body'],
            'post': post_instance,
        }
        return self.dal.insert_comment(data)
