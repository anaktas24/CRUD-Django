from django.shortcuts import render
from .models import Posts

def posts_list(request):
    return render(request, 'posts/posts_list.html')
