from django.shortcuts import get_object_or_404
from project.models import Post


class PostDAL:
    @staticmethod
    def retrieve_post(pk):
        return get_object_or_404(Post, pk=pk)

    @staticmethod
    def get_posts_list():
        return Post.objects.all()

    @staticmethod
    def delete_post(pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()

    @staticmethod
    def insert_post(object_data: dict):
        Post.objects.create(**object_data)

    @staticmethod
    def update_post(object_data: dict, pk):
        post = get_object_or_404(Post, pk=pk)
        post.body = object_data['body']
        post.header = object_data['header']
        post.save()
