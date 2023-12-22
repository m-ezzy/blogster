from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'content', 'author', 'status']

class CommentForm(ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'content', 'author', 'status']
