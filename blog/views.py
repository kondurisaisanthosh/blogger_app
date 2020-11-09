from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# posts=[
#     {
#         'author' : 'sai',
#         'title' : 'post1',
#         'content' : 'first post content',
#         'date' : 'august 10'
#     }
# ]

# @login_required
# def home(request):
#     # return HttpResponse('<h1>Hello World</h1>')
#     context={
#         'posts':Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 4
# <app>/<model>_<viewtype>.html=blog/post_list.html

class UserPostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')



class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



class MyPostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name = 'blog/myposts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')
