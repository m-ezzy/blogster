from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

#####################################################################################################################################

# class Profile(models.Model):
#   profile_id = models.BigAutoField(primary_key=True)
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   name = models.CharField(max_length=80)
#   email = models.EmailField()
#   # image = models.ImageField(default="default.png", upload_to="profile_pics")

#   def __str__(self):
#     return f"{self.user.username} Profile"

#####################################################################################################################################

class Category(models.Model):
  # category_id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

#####################################################################################################################################

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

class Post(models.Model):
  # post_id = models.BigAutoField(primary_key=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',default=1)
  categories = models.ManyToManyField(Category, related_name="posts")
  title = models.CharField(max_length=200, unique=True)
  content = models.TextField(max_length=2000)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  published_on = models.DateTimeField(default=timezone.now)
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title

#####################################################################################################################################

class Comment(models.Model):
  # comment_id = models.BigAutoField(primary_key=True)
  commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',default=1)
  post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',default=1)
  content = models.TextField(max_length=500)
  created_on = models.DateTimeField(auto_now_add=True)

  # class Meta:
  #   model = Comment
  #   ordering = ['created_on']

  def __str__(self):
    # return 'Comment {} by {}'.format(self.content, self.commentor)
    return f"{self.commentor} on '{self.post}'"

#####################################################################################################################################
