from django.forms import ModelForm
from .models import Category, Post, Comment

class CategoryFilterForm(ModelForm):
  class Meta:
    model = Category
    fields = ['name']

class PostCreateForm(ModelForm):
  class Meta:
    model = Post
    fields = ['categories', 'title', 'content', 'status']

class PostEditForm(ModelForm):
  class Meta:
    model = Post
    fields = ['categories', 'title', 'content', 'status']

class PostDeleteForm(ModelForm):
  class Meta:
    model = Post
    fields = ['categories', 'title', 'content', 'status']

class CommentCreateForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']

class CommentEditForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']

class CommentDeleteForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
