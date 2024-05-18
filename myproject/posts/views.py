from django.shortcuts import render

def posts_list(request):
    return render(request, 'posts/posts_list.html')
