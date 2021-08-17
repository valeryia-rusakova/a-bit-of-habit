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
        post = Post.objects.get(pk=pk)
        post.delete()
