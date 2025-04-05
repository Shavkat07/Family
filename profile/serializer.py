from rest_framework import serializers

from custom_auth.serializers import CustomUserSerializer
from .models import Profile, Health, Document, DocumentCategory


class ProfileSerializer(serializers.ModelSerializer):
	user = CustomUserSerializer(read_only=True)
	class Meta:
		model = Profile
		fields = '__all__'  # Можно указать конкретные поля, если не нужны все
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


class DocumentCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = DocumentCategory
		fields = '__all__'
