from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
	RegisterView, CustomTokenObtainPairView, LogoutView, ProfileUserView,
	UserViewSet, SetNewPasswordView, ChangePasswordView, ResetPasswordView
)


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
	# Аутентификация
	path('register/', RegisterView.as_view(), name='register'),
	path('login/', CustomTokenObtainPairView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),

	# Токены
	path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

	# Профиль пользователя
	path('profile/', ProfileUserView.as_view(), name='profile'),

	# Смена пароля
	path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
	path('change-password/', ChangePasswordView.as_view(), name='change-password'),

	# Восстановление пароля
	path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
] + router.urls
