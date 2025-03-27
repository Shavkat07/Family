from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Post, PostImage, PostCategory, Comment
from .serializer import PostSerializer, PostImageSerializer, PostCategorySerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets


# Create your views here.
class PostCategoryViewSet(viewsets.ModelViewSet):
	queryset = PostCategory.objects.all()
	serializer_class = PostCategorySerializer
	permission_classes = (IsAuthenticatedOrReadOnly, )


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

class PostImageViewSet(viewsets.ModelViewSet):
	queryset = PostImage.objects.all()
	serializer_class = PostImageSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	parser_classes = (MultiPartParser, FormParser)

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, ]





