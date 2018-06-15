from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title' , 'content',  'category', 'photo', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['category_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['author', 'message']
