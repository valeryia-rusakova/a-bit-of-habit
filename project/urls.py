from django.urls import include, path
from project.views.post import PostView
urlpatterns = [
    path('', PostView.as_view({'get': 'list'}), name="list_posts"),
    path('<int:pk>', PostView.as_view({'get': 'retrieve'}), name="retrieve_post"),
]