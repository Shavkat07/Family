from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Health, Profile, DocumentCategory, Document
from .permissions import IsOwner
from .serializers import ProfileSerializer, HealthSerializer, DocumentSerializer, DocumentCategorySerializer


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated, IsOwner]

	def get_queryset(self):
		# Только профиль текущего пользователя
		return Profile.objects.filter(user=self.request.user)

	def list(self, request, *args, **kwargs):
		# Отключаем список всех профилей
		return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def create(self, request, *args, **kwargs):
		# Проверяем, есть ли уже профиль
		if Profile.objects.filter(user=request.user).exists():
			return Response({"detail": "Profile already exists."}, status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(user=request.user)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def perform_update(self, serializer):
		# Обновление только своего профиля
		serializer.save(user=self.request.user)

	def destroy(self, request, *args, **kwargs):
		# Удаление только своего профиля
		instance = self.get_object()
		if instance.user != request.user:
			return Response({"detail": "You can only delete your own profile."}, status=status.HTTP_403_FORBIDDEN)
		return super().destroy(request, *args, **kwargs)

	@action(detail=False, methods=['get'], url_path='me')
	def get_own_profile(self, request):
		try:
			profile = Profile.objects.get(user=request.user)
			serializer = self.get_serializer(profile)
			return Response(serializer.data)
		except Profile.DoesNotExist:
			return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)


class HealthViewSet(viewsets.ModelViewSet):
	queryset = Health.objects.all()
	serializer_class = HealthSerializer
	permission_classes = (IsAuthenticated,)


class DocumentViewSet(viewsets.ModelViewSet):
	queryset = Document.objects.all()
	serializer_class = DocumentSerializer
	permission_classes = (IsAuthenticated, IsOwner)

	def get_queryset(self):
		return Document.objects.filter(user=self.request.user)

	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(user=request.user)  # Привязываем к текущему пользователю
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def perform_update(self, serializer):
		# Обновляем только для текущего пользователя
		serializer.save(user=self.request.user)

	def destroy(self, request, *args, **kwargs):
		# Удаляем только свой документ
		instance = self.get_object()
		return super().destroy(request, *args, **kwargs)


class DocumentCategoryViewSet(viewsets.ModelViewSet):
	queryset = DocumentCategory.objects.all()
	serializer_class = DocumentCategorySerializer
	permission_classes = (IsAuthenticated,)
