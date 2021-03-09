from django.contrib import admin
from django.urls import path, include
from post import views as post_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', post_views.PostListView.as_view(), name="posts"),
    path('post/<int:pk>/', post_views.PostDetailView.as_view(), name="post-detail"),
    # path('posts/', account_views.posts, name='posts'),
    path('post/new/<title/', post_views.PostCreateView.as_view(), name="post-create"),


] 