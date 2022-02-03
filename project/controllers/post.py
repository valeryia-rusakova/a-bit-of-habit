from project.controllers.controller import Controller
from project.dal.post import PostDAL


class PostController(Controller):
    dal = PostDAL()

    def get_queryset(self, request, request_type):
        if request_type == 'list':
            return self.dal.get_posts_list()
        post_pk = request.parser_context['kwargs']['pk']
        return self.dal.retrieve_post(post_pk)

    def create(self, request):
        data = {
            'user': request.user,
            'header': request.data['header'],
            'body': request.data['body']
        }
        return self.dal.insert_post(data)

    def delete(self, request):
        delete_pk = request.parser_context['kwargs']['pk']
        return self.dal.delete_post(delete_pk)

    def update(self, request):
        data = {}
        if request.data['header']:
            data.update({'header': request.data['header']})
        if request.data['body']:
            data.update({'body': request.data['body']})
        update_pk = request.parser_context['kwargs']['pk']
        return self.dal.update_post(object_data=data, pk=update_pk)

    def get_extra_posts(self, request):
        return self.dal.get_extra_posts(request.user)
