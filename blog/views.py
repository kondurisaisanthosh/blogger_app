from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required


# posts=[
#     {
#         'author' : 'sai',
#         'title' : 'post1',
#         'content' : 'first post content',
#         'date' : 'august 10'
#     },
#     {
#         'author' : 'santosh',
#         'title' : 'post2',
#         'content' : 'second post content',
#         'date' : 'august 11'
#     },
#     {
#         'author' : 'sandeep',
#         'title' : 'post3',
#         'content' : 'third post content',
#         'date' : 'august 12'
#     }
# ]

@login_required
def home(request):
    # return HttpResponse('<h1>Hello World</h1>')
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def myposts(request):
    return render(request,'blog/myposts.html',{'title':'myposts'})
