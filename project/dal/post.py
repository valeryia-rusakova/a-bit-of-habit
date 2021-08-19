from project.models import Post


class PostDAL:
    @staticmethod
    def post_retrieve(pk):
        return Post.objects.get(pk=pk)

    @staticmethod
    def post_list():
        return Post.objects.all()

    @staticmethod
    def post_delete(pk):
        print(pk)
        post = Post.objects.get(pk=pk)
        post.delete()

    @staticmethod
    def post_create(object_data: dict):
        Post.objects.create(**object_data)

    @staticmethod
    def post_update(object_data: dict, pk):
        post = Post.objects.get(pk=pk)
        post.body = object_data['body']
        post.header = object_data['header']
        post.save()
