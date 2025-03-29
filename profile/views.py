from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Health, Profile, DocumentCategory, Document
from .serializer import ProfileSerializer, HealthSerializer, DocumentSerializer, DocumentCategorySerializer


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = (IsAuthenticated,)


class HealthViewSet(viewsets.ModelViewSet):
	queryset = Health.objects.all()
	serializer_class = HealthSerializer
	permission_classes = (IsAuthenticated,)


class DocumentViewSet(viewsets.ModelViewSet):
	queryset = Document.objects.all()
	serializer_class = DocumentSerializer
	permission_classes = (IsAuthenticated,)


class DocumentCategoryViewSet(viewsets.ModelViewSet):
	queryset = DocumentCategory.objects.all()
	serializer_class = DocumentCategorySerializer
	permission_classes = (IsAuthenticated,)
