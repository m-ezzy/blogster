from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Category, Post, Comment
from .forms import CategoryFilterForm, PostCreateForm, PostEditForm, PostDeleteForm, CommentCreateForm, CommentEditForm, CommentDeleteForm

#####################################################################################################################################

def about(request):
  return render(request, 'about.html')

def home(request):
  context = {
    "posts": Post.objects.filter(status=1),
    "categories": Category.objects.all(),
    "forms": {
      "post_delete": PostDeleteForm(),
      "category_filter": CategoryFilterForm(), # for filtering posts by category
    }
  }
  return render(request, 'home.html', context)

#####################################################################################################################################

@login_required
def display_posts(request):
  # only posts created by logged in user should be displayed
  context = {
    "posts": {
      "published": Post.objects.filter(author=request.user, status=1),
      "draft": Post.objects.filter(author=request.user, status=0),
    }
  }
  return render(request, 'posts/posts.html', context)

def display_post(request, pk):
  post = Post.objects.get(pk=pk)

  if post.status == 0 and post.author != request.user:
    return render(request, 'message.html', { "message": 'You are not allowed to view this post.'}, status=403)

  comments = Comment.objects.filter(post=post)
  context = {
    "post": post,
    "comments": comments,
    "forms": {
      "post_delete": PostDeleteForm(),
      "comment_create": CommentCreateForm(),
    }
  }
  return render(request, 'posts/post.html', context)

@login_required
def create_post(request):
  if request.method == 'GET':
    context = {
      'form': PostCreateForm()
    }
    return render(request, 'posts/create.html', context)
  else:
    form = PostCreateForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect(f"/posts/{post.pk}")

@login_required
def edit_post(request, pk): # pk id
  post = Post.objects.get(pk=pk)

  if post.author != request.user:
    return render(request, 'message.html', { "message": 'You are not allowed to edit this post.'}, status=403)

  if request.method == 'GET':
    context = {
      'form': PostEditForm(instance=post)
    }
    return render(request, 'posts/edit.html', context)
  else:
    form = PostEditForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect(f"/posts/{pk}")
      # return render(request, 'posts/post.html', { "post": post })

@login_required
def delete_post(request, pk):
  if request.method == 'POST':
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
      return render(request, 'message.html', { "message": 'You are not allowed to delete this post.'}, status=403)
    else:
      post.delete()
      return redirect("/posts")

#####################################################################################################################################

@login_required
def display_comments(request):
  # display all the comments created by logged in user
  context = {
    "comments": Comment.objects.filter(commentor=request.user),
    "form": CommentDeleteForm(),
  }
  return render(request, 'comments/comments.html', context)

@login_required
def create_comment(request):
  form = CommentCreateForm(request.POST)
  if form.is_valid():
    comment = form.save(commit=False)
    comment.post = Post.objects.get(pk=request.POST['post_id'])
    comment.commentor = request.user
    comment.save()
    return redirect(f"/posts/{comment.post.pk}")

@login_required
def edit_comment(request, pk):
  comment = Comment.objects.get(pk=pk)

  if comment.commentor != request.user:
    return render(request, 'message.html', { "message": 'You are not allowed to edit this comment.'}, status=403)
  
  if request.method == 'GET':
    context = {
      'form': CommentEditForm(instance=comment)
    }
    return render(request, 'comments/edit.html', context)
  elif request.method == 'POST':
    form = CommentEditForm(request.POST, instance=comment)
    if form.is_valid():
      form.save()
      return redirect("/comments")
      # return render(request, 'comments/view_list.html', { "post": post })

@login_required
def delete_comment(request, pk):
  if request.method == 'POST':
    comment = get_object_or_404(Comment, pk=pk)
    
    if comment.commentor != request.user:
      return render(request, 'message.html', { "message": 'You are not allowed to delete this comment.'}, status=403)
    else:
      comment.delete()
      return redirect(f"/posts/{comment.post.pk}")

#####################################################################################################################################

# a separate page for each category to view posts of that category
def display_category_posts(request, name):
  posts = Post.objects.filter(categories__name__contains=name).order_by("-created_on")
  context = {
    "category_name": name,
    "posts": posts,
    "forms": {
      "post_delete": PostDeleteForm(),
    }
  }
  return render(request, "category/category_posts.html", context)

# in home page, user can select one or more than one category to view posts on the same page
def display_filter_posts(request):
  if request.method == 'GET':
    context = {
      "posts": Post.objects.filter(status=1),
      "categories": Category.objects.all(),
      # "form": CategoryFilterForm(), # for filtering posts by category
      "form": PostDeleteForm(),
    }
    return render(request, 'home.html', context)
  elif request.method == 'POST':
    form = CategoryFilterForm(request.POST)
    if form.is_valid():
      category = form.cleaned_data['category']
      posts = Post.objects.filter(categories__name__contains=category)
      # context = {
        # "posts": posts,
        # "categories": Category.objects.all()
      # }
      # return render(request, 'home.html', context)
      # return redirect(f"/category/{category}")
      return redirect("/")
  else:
    form = CategoryFilterForm(request.POST)
    if form.is_valid():
      category = form.cleaned_data['category']
      posts = Post.objects.filter(categories__name__contains=category)
      # context = {
        # "posts": posts,
        # "categories": Category.objects.all()
      # }
      # return render(request, 'home.html', context)
      # return redirect(f"/category/{category}")
      return redirect("/")

#####################################################################################################################################

def display_user(request, pk):
  user = User.objects.get(pk=pk)
  context = {
    "user": user,
  }
  return render(request, "users/user.html", context)

#####################################################################################################################################
