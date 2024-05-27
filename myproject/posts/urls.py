from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"), # paths matter how we written them
    path('new_post/', views.post_new, name="new_post"),
    path('<slug:slug>', views.post_page, name="page"),
]
