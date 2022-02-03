from project.models import Comment
from project.dal.MetaDAL import MetaDAL


class CommentDAL(metaclass=MetaDAL):
    @staticmethod
    def get_comments_list():
        return Comment.objects.all()

    @staticmethod
    def insert_comment(object_data: dict):
        Comment.objects.create(**object_data)
