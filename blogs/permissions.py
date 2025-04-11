from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
	"""
	Разрешает доступ только для чтения всем пользователям,
	а полный доступ — только если user_type == 'admin'
	"""

	def has_permission(self, request, view):
		# Разрешить безопасные методы (GET, HEAD, OPTIONS) всем
		if request.method in SAFE_METHODS:
			return True

		# Только если пользователь авторизован и его тип — admin
		return request.user.is_authenticated and getattr(request.user, 'user_type', None) == 'admin'
