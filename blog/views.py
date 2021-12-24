from django.shortcuts import render
from .models import Post

posts = [
    {
        'title': 'Title1',
        'author': 'author1'
    },
    {
        'title': 'Title2',
        'author': 'author2'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'NEW TITLE'
    }
    return render(request, 'blog/blog.html', context)
