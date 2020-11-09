from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from users import views as u_views

urlpatterns = [
    # path('home',views.home,name='blog-home'),
    path('home',PostListView.as_view(),name='blog-home'),
    path('home/user/<username>',UserPostListView.as_view(),name='user-posts'),
    path('home/post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('home/post/new', PostCreateView.as_view(), name='post-create'),
    path('home/post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('home/post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('myposts/',views.myposts,name='blog-myposts'),
]
