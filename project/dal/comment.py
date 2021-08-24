from project.models import Comment


class CommentDAL:
    @staticmethod
    def retrieve_comment(pk):
        return Comment.objects.get(pk=pk)

    @staticmethod
    def get_comments_list():
        return Comment.objects.all()

    @staticmethod
    def delete_comment(pk):
        print(pk)
        comment = Comment.objects.get(pk=pk)
        comment.delete()

    @staticmethod
    def insert_comment(object_data: dict):
        Comment.objects.create(**object_data)

    @staticmethod
    def update_comment(object_data: dict, pk):
        comment = Comment.objects.get(pk=pk)
        comment.body = object_data['body']
        comment.post = object_data['post']
        comment.save()
