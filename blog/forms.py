from django.forms import ModelForm, TextInput, Textarea, Select, SelectMultiple
from .models import Category, Post, Comment

widgets = {
  'categories': SelectMultiple(attrs={'class': 'form-control'}),
  'title': TextInput(attrs={'class': 'form-control'}),
  'content': Textarea(attrs={'class': 'form-control'}),
  'status': Select(attrs={'class': 'form-control'}),
}

#####################################################################################################################################

class CategoryFilterForm(ModelForm):
  class Meta:
    model = Category
    fields = ['name']

#####################################################################################################################################

class PostCreateForm(ModelForm):
  class Meta:
    model = Post
    fields = ['categories', 'title', 'content', 'status']
    widgets = widgets

class PostEditForm(ModelForm):
  class Meta:
    model = Post
    fields = ['categories', 'title', 'content', 'status']
    widgets = widgets

class PostDeleteForm(ModelForm):
  class Meta:
    model = Post
    fields = []

#####################################################################################################################################

class CommentCreateForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
    widgets = {
      'content': TextInput(attrs={
        'rows': 1,
        'class': 'form-control h-25',
        'placeholder': 'Leave a comment...'
      }),
    },
    labels = {
      'content': ''
    }

class CommentEditForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
    widgets = {
      'content': Textarea(attrs={
        'class': 'form-control'
      }),
    }

class CommentDeleteForm(ModelForm):
  class Meta:
    model = Comment
    fields = []

#####################################################################################################################################
