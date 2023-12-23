from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Category, Post, Comment
from .forms import CategoryFilterForm, PostCreateForm, PostEditForm, PostDeleteForm, CommentCreateForm, CommentEditForm, CommentDeleteForm

def about(request):
  return render(request, 'about.html')

def home(request):
  if request.method == 'POST':
    form = CategoryFilterForm(request.POST)
    if form.is_valid():
      category = form.cleaned_data['category']
      posts = Post.objects.filter(categories__name__contains=category)
      context = {
        "posts": posts,
        "categories": Category.objects.all()
      }
      return render(request, 'home.html', context)
      # return redirect(f"/category/{category}")
      # return redirect("/")
  else:
    context = {
      "posts": Post.objects.all(),
      "categories": Category.objects.all()
    }
    return render(request, 'home.html', context)

def display_posts(request):
  # only posts created by logged in user should be displayed
  context = { "posts": Post.objects.filter(author=request.user) }
  return render(request, 'posts/posts.html', context)

def create_post(request):
  if request.method == 'GET':
    context = { 'form': PostCreateForm() }
    return render(request, 'posts/create.html', context)
  else:
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()

      return redirect("/posts")

def display_post(request, pk):
  post = Post.objects.get(pk=pk)
  comments = Comment.objects.filter(post=post)
  context = {
    "post": post,
    "comments": comments,
  }
  return render(request, 'posts/post.html', context)

def update_post(request, pk): # pk id
  if request.method == 'GET':
    context = { 'form': PostEditForm(instance=Post.objects.get(pk=pk)) }
    return render(request, 'posts/update.html', context)
  else:
    form = PostEditForm(request.POST or None, request.FILES or None)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
      # return HttpResponse('<h1>refdc</h1>')
      # return redirect("/posts")
      return render(request, 'posts/post.html', { "post": post })
    else:
      return HttpResponse('<h1>invalid</h1>')

def delete_post(request, pk):
  return(HttpResponse('<h1>delete post form</h1>'))

def display_comments(request):
  # display all the comments created by logged in user
  context = { "comments": Comment.objects.filter(commentor=request.user) }
  return render(request, 'comments/view_list.html', context)

def create_comment(request):
  return(HttpResponse('<h1>create comment form</h1>'))

def edit_comment(request, pk):
  if request.method == 'GET':
    context = { 'form': CommentEditForm(instance=Comment.objects.get(pk=pk)) }
    return render(request, 'comments/edit.html', context)
  elif request.method == 'POST':
    form = CommentEditForm(request.POST)
    if form.is_valid():
      comment = form.save()
      comment.save()
      # return HttpResponse('<h1>refdc</h1>')
      return redirect("/comments")
      # return render(request, 'comments/view_list.html', { "post": post })
    else:
      return HttpResponse('<h1>invalid comment</h1>')

def delete_comment(request, pk):
  comment = Comment.objects.get(pk=pk).delete()
  return redirect("/comments")

def display_category_posts(request, name):
  posts = Post.objects.filter(
    categories__name__contains=name
  ).order_by("-created_on")
  context = {
    "category_name": name,
    "posts": posts,
  }
  return render(request, "category/display_category_posts.html", context)
