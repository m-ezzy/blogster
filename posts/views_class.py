# 2 types of views: function-based and class-based

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostList(ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'home.html'

class PostDetail(DetailView):
  model = Post
  template_name = 'posts/view_detail.html'

class PostCreate(CreateView):
  model = Post
  fields = ['title', 'content', 'author', 'category']
  template_name = 'posts/create.html'
  # form_class = PostForm
