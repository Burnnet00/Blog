from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

class PostView(View):
    '''Vievs'''
    def get (self, reguest):
        posts = Post.objects.all()
        return render(reguest, 'blog/blog.html', {'post_list': posts})

class PostDetail(View):
    def get (self, reguest, pk):
        post = Post.objects.get(id=pk)
        return render(reguest, 'blog/blog_detail.html', {'post': post})
