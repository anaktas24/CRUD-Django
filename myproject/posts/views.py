from django.shortcuts import render
from .models import Posts

def posts_list(request):
    posts = Posts.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})
