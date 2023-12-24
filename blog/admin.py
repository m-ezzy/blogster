from django.contrib import admin
from .models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
  pass

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'status','created_on')
  list_filter = ("status",)
  search_fields = ['title', 'content']
  # prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
  pass

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#   list_display = ('name', 'body', 'post', 'created_on', 'active')
#   list_filter = ('active', 'created_on')
#   search_fields = ('name', 'email', 'body')
#   actions = ['approve_comments']

#   def approve_comments(self, request, queryset):
#     queryset.update(active=True)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
