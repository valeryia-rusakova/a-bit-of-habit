from django.contrib.auth import get_user_model
from django.db.models import Count, Avg

from project.dal.MetaDAL import MetaDAL

User = get_user_model()


class UserDAL(metaclass=MetaDAL):

    @staticmethod
    def insert_user(object_data: dict):
        User.objects.create_user(**object_data)

    @staticmethod
    def get_avg_num_posts():
        return User.objects.annotate(num_posts=Count('post')).aggregate(Avg('num_posts'))
