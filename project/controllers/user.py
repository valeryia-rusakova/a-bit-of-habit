from project.dal.user import UserDAL


class UserController:
    dal = UserDAL()

    def create_user(self, request):
        data = {
            'username': request.data['username'],
            'email': request.data['email'],
            'password': request.data['password']
        }
        return self.dal.insert_user(data)
