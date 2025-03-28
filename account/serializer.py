from rest_framework import serializers

from .models import Profile, Health, Document, DocumentCategory


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'  # Можно указать конкретные поля, если не нужны все


class HealthSerializer(serializers.ModelSerializer):
	class Meta:
		model = Health
		fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = '__all__'


class DocumentCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = DocumentCategory
		fields = '__all__'
