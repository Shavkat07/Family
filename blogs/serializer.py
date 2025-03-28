from rest_framework import serializers

from .models import Post, PostImage, PostCategory, Comment


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'  # Можно указать конкретные поля, если не нужны все


class PostImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostImage
		fields = '__all__'




class PostCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = PostCategory
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
