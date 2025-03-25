from django.contrib import admin

from blogs.models import Comment, Post, PostCategory

# Register your models here.
admin.site.register([Comment, Post, PostCategory])