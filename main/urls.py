from django.urls import path, include
from .import views
from main.views import Home, PostsListView
urlpatterns = [
    path('', Home.as_view(), name='main-home'),
    path('post', PostsListView.as_view(), name='posts'),
]
