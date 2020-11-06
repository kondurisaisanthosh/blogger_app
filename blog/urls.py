from django.urls import path
from . import views
from users import views as u_views

urlpatterns = [
    path('home',views.home,name='blog-home'),
    path('myposts/',views.myposts,name='blog-myposts'),
]
