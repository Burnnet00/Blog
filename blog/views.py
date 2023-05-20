from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm

class PostView(View):
    '''Vievs'''
    def get (self, reguest):
        posts = Post.objects.all()
        return render(reguest, 'blog/blog.html', {'post_list': posts})

class PostDetail(View):
    '''Viev'''
    def get (self, reguest, pk):
        post = Post.objects.get(id=pk)
        return render(reguest, 'blog/blog_detail.html', {'post': post})

class AddComment(View):
    '''add comments'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')
