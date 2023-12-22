from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from .models import Post, Comment
from .forms import PostForm

# posts = [
#   {
#     'title': 'Beautiful is better than ugly',
#     'author': 'John Doe',
#     'content': 'Beautiful is better than ugly',
#     'published_at': 'October 1, 2022'
#   },
#   {
#     'title': 'Explicit is better than implicit',
#     'author': 'Jane Doe',
#     'content': 'Explicit is better than implicit',
#     'published_at': 'October 1, 2022'
#   }
# ]

def display_posts(request):
  # context = { 'posts': posts }
  context = { "posts": Post.objects.all() }
  return render(request, 'posts/display.html', context)


# def post(request, slug):
#     return HttpResponse('<h1>single post details</h1>')


def create_post(request):
  if request.method == 'GET':
    context = {
      'form': PostForm()
    }
    return render(request, 'posts/create.html', context)
  else:
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
      post = form.save(commit=False)
      post.slug = slugify(post.title)
      post.author = request.user
      post.save()

      return redirect("/posts")


def display_comments(request):
  context = { "comments": Comment.objects.all() }
  return render(request, 'comments/display.html', context)

def create_comment(request):
  return(HttpResponse('<h1>create comment form</h1>'))

def home(request):
  context = { "posts": Post.objects.all() }
  
  # return HttpResponse('<h1>Blog Home</h1>')
  return render(request, 'home.html')


def about(request):
  # return HttpResponse('<h1>About</h1>')
  return render(request, 'about.html')


