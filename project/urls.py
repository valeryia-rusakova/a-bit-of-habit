from django.urls import path
from project.views.comment import CommentView
from project.views.image import ImageView
from project.views.post import PostView

urlpatterns = [
    path('posts/', PostView.as_view({'get': 'list', 'post': 'create'}), name="posts_list"),
    path('posts/<int:pk>/', PostView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="post_detail"),
    path('comments/', CommentView.as_view({'get': 'list', 'post': 'create'}), name="comments_list"),
    path('comments/<int:pk>/', CommentView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="comment_detail"),
    path('images/', ImageView.as_view({'get': 'list', 'post': 'create'}), name="images_list"),
    path('images/<int:pk>/', ImageView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="image_detail"),
]
