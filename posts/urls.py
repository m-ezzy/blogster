from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('', views.PostList.as_view(), name='home'),

  path('posts', views.display_posts, name='dispaly_posts'),
  path('posts/create', views.create_post, name='create_post'),

  # path('post/<str:slug>', views.post, name='post'),
  # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),


  path('comments', views.display_comments, name='dispaly_comments'),
  path('comments/create', views.create_comment, name='create_comment'),

  path('about/', views.about, name='about'),
]
