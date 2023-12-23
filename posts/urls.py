from django.urls import path
from . import views

# app_name = 'posts'
urlpatterns = [
  path('about/', views.about, name='about'),

  path('', views.home, name='home'),
  # path('', views.PostList.as_view(), name='home'),

  path('posts', views.display_posts, name='dispaly_posts'),
  path('posts/create', views.create_post, name='create_post'),
  path('posts/<int:pk>', views.display_post, name='display_post'),
  path('posts/<int:pk>/update', views.update_post, name='update_post'),
  path('posts/<int:pk>/delete', views.delete_post, name='delete_post'),

  path('comments', views.display_comments, name='dispaly_comments'),
  path('comments/create', views.create_comment, name='create_comment'),
  path('comments/<int:pk>/edit', views.edit_comment, name='edit_comment'),
  path('comments/<int:pk>/delete', views.delete_comment, name='delete_comment'),

  path('category/<str:name>', views.display_category_posts, name='display_category_posts'),
]
