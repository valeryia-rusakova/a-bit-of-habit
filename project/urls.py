from django.urls import path

from project.views.achievement_user import AchievementUserView
from project.views.habit_user import HabitUserView
from project.views.achievement import AchievementView
from project.views.comment import CommentView
from project.views.habit import HabitView
from project.views.image import ImageView
from project.views.post import PostView
from project.views.user import RegistrationAPIView, LoginAPIView, StatisticAPIView

urlpatterns = [
    path('posts/', PostView.as_view({'get': 'list', 'post': 'create'}), name="posts_list"),
    path('posts/<int:pk>/', PostView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="post_detail"),
    path('posts/extra_posts/', PostView.as_view({'get': 'get_extra_posts'}),
         name="get_extra_posts"),
    path('comments/', CommentView.as_view({'get': 'list', 'post': 'create'}), name="comments_list"),
    path('images/', ImageView.as_view({'get': 'list', 'post': 'create'}), name="images_list"),
    path('images/<int:pk>/', ImageView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="image_detail"),
    path('habits/', HabitView.as_view({'get': 'list', 'post': 'create'}), name="habits_list"),
    path('habits/<int:pk>/', HabitView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="habit_detail"),
    path('achievements/', AchievementView.as_view({'get': 'list', 'post': 'create'}), name="achievements_list"),
    path('achievements/<int:pk>/', AchievementView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name="achievement_detail"),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('habitUser/', HabitUserView.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update'}),
         name="habits_users_list"),
    path('habitUser/get_max_days_checked/', HabitUserView.as_view({'get': 'get_max_days_checked'}),
         name="habits_users_get_max_days_checked"),
    path('userAchievements/', AchievementUserView.as_view({'get': 'list'}),
         name="achievements_users_list"),
    path('users/statistic/', StatisticAPIView.as_view()),
]
