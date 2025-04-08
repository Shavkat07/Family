from rest_framework import serializers
from rest_framework.fields import ImageField

from custom_auth.serializers import CustomUserSerializer
from .models import Profile, Health, Document, DocumentCategory


class ProfileSerializer(serializers.ModelSerializer):
	user = CustomUserSerializer(read_only=True)
	avatar = ImageField(required=False)

	class Meta:
		model = Profile
		fields = ['id', 'phone', 'avatar', 'bio', 'birthday', 'user_type',
		          'user']  # Можно указать конкретные поля, если не нужны все
		read_only_fields = ['user']


class HealthSerializer(serializers.ModelSerializer):
	class Meta:
		model = Health
		fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = '__all__'
		read_only_fields = ['user']

	def validate_file(self, value):
		valid_mime_types = [
			'application/pdf',
			'application/msword',  # .doc
			'application/vnd.openxmlformats-officedocument.wordprocessingml.document',  # .docx
			'image/jpeg',
			'image/png',
			'image/gif',
			'image/webp',
		]
		mime_type = value.content_type
		if mime_type not in valid_mime_types:
			raise serializers.ValidationError("Разрешены только изображения, PDF и Word-документы.")
		return value


class DocumentCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = DocumentCategory
		fields = '__all__'
