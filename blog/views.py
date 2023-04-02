from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

class PostView(View):
    '''Vievs'''
    def get (self, reguest):
        posts = Post.objects.all()
        return render(reguest, 'blog/blog.html', {'post_list': posts})
# Create your views here.
