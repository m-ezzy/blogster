# 2 types of views: function-based and class-based

from typing import Any
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

class PostEdit(UpdateView):
  model = Post
  fields = ['title', 'content', 'author', 'category']
  template_name = 'posts/edit.html'
  
  def get_object(self):
    obj = super().get_object()
    if obj.author != self.request.user:
      raise PermissionDenied()
    return obj
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class PostDelete(DeleteView):
  model = Post
  template_name = 'posts/delete.html'
  success_url = '/'
