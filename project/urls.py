from django.urls import path
from project.views.achievement import AchievementView
from project.views.comment import CommentView
from project.views.habit import HabitView
from project.views.image import ImageView
from project.views.post import PostView
from project.views.profile import ProfileView

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
    path('habits/', HabitView.as_view({'get': 'list', 'post': 'create'}), name="habits_list"),
    path('habits/<int:pk>/', HabitView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="habit_detail"),
    path('achievements/', AchievementView.as_view({'get': 'list', 'post': 'create'}), name="achievements_list"),
    path('achievements/<int:pk>/', AchievementView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="achievement_detail"),
    path('profiles/', ProfileView.as_view({'get': 'list'}), name="profiles_list"),
    path('profiles/<int:pk>/', ProfileView.as_view({'get': 'retrieve', 'put': 'update'}),
         name="profile_detail"),
]
