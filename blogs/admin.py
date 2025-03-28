from django.contrib import admin

from blogs.models import Comment, Post, PostCategory, PostImage


admin.site.register([Comment, Post, PostCategory, PostImage])

