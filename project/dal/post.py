from project.models import Post


class PostDAL:
    @staticmethod
    def retrieve_post(pk):
        return Post.objects.get(pk=pk)

    @staticmethod
    def get_list_posts():
        return Post.objects.all()

    @staticmethod
    def delete_post(pk):
        print(pk)
        post = Post.objects.get(pk=pk)
        post.delete()

    @staticmethod
    def insert_post(object_data: dict):
        Post.objects.create(**object_data)

    @staticmethod
    def update_post(object_data: dict, pk):
        post = Post.objects.get(pk=pk)
        post.body = object_data['body']
        post.header = object_data['header']
        post.save()
