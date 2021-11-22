from django.contrib.auth import get_user_model

User = get_user_model()


class UserDAL:

    @staticmethod
    def insert_user(object_data: dict):
        User.objects.create_user(**object_data)