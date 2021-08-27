from django.shortcuts import get_object_or_404
from project.models import Comment


class CommentDAL:
    @staticmethod
    def retrieve_comment(pk):
        return get_object_or_404(Comment, pk=pk)

    @staticmethod
    def get_comments_list():
        return Comment.objects.all()

    @staticmethod
    def delete_comment(pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()

    @staticmethod
    def insert_comment(object_data: dict):
        Comment.objects.create(**object_data)

    @staticmethod
    def update_comment(object_data: dict, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.body = object_data['body']
        comment.post = object_data['post']
        comment.save()
