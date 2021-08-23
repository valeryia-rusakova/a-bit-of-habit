from django.urls import path
from project.views.post import PostView

urlpatterns = [
    path('', PostView.as_view({'get': 'list', 'post': 'create'}), name="posts_list"),
    path('<int:pk>/', PostView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name="post_detail"),
]
