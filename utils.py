from rest_framework.exceptions import PermissionDenied


def has_permissions(permission):
    roles = {
        'admin': ['user_admin'],
        'user': ['user_admin', 'user_authenticated'],
        'anonymous': ['user_any', 'user_admin', 'user_authenticated'],
    }

    def decorator(view_method):
        def wrapper(self, *args, **kwargs):
            user = self.request.user
            if user.is_anonymous:
                user_role = 'user_any'
            elif user.is_superuser:
                user_role = 'user_admin'
            else:
                user_role = 'user_authenticated'
            if user_role in roles[permission]:
                return view_method(self, *args, **kwargs)
            else:
                raise PermissionDenied()

        return wrapper

    return decorator
