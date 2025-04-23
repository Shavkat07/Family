from rest_framework import serializers


from .models import Post, PostImage, PostCategory, Comment
from .permissions import IsAdminOrReadOnly

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'  # Можно указать конкретные поля, если не нужны все
		permission_classes = IsAdminOrReadOnly

class PostImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostImage
		fields = '__all__'
		permission_classes = IsAdminOrReadOnly



class PostCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = PostCategory
		fields = '__all__'
		permission_classes = IsAdminOrReadOnly

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
