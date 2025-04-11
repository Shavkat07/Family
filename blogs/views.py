from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, PostImage, PostCategory, Comment
from .permissions import IsAdminOrReadOnly
from .serializer import PostSerializer, PostImageSerializer, PostCategorySerializer, CommentSerializer


# Create your views here.
class PostCategoryViewSet(viewsets.ModelViewSet):
	queryset = PostCategory.objects.all()
	serializer_class = PostCategorySerializer
	permission_classes = [IsAdminOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [IsAdminOrReadOnly]


class PostImageViewSet(viewsets.ModelViewSet):
	queryset = PostImage.objects.all()
	serializer_class = PostImageSerializer
	permission_classes = [IsAdminOrReadOnly]
	parser_classes = (MultiPartParser, FormParser)


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticatedOrReadOnly ]
