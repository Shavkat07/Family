from allauth.account.views import ConfirmEmailView
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
# from .views import UserViewSet
# from .views import (
	# RegisterView, CustomTokenObtainPairView, LogoutView, ProfileUserView,
	# UserViewSet, SetNewPasswordView, ChangePasswordView, ResetPasswordView
# )

# router = DefaultRouter()
# router.register('users', UserViewSet, basename='users')

urlpatterns = [
	              # API аутентификации
	path('', include('dj_rest_auth.urls')),
	re_path(
		"^registration/account-confirm-email/(?P<key>[-:\w]+)/$",
		ConfirmEmailView.as_view(),
		name="account_confirm_email",
	),
	path('registration/', include('dj_rest_auth.registration.urls')),
	path('social/', include('allauth.socialaccount.urls')),


	# Аутентификация
	# path('register/', RegisterView.as_view(), name='register'),
	# path('login/', CustomTokenObtainPairView.as_view(), name='login'),
	# path('logout/', LogoutView.as_view(), name='logout'),
	#
	# # Токены
	# path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	#
	# # Профиль пользователя
	# path('profile/', ProfileUserView.as_view(), name='profile'),
	#
	# # Смена пароля
	# path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
	# path('change-password/', ChangePasswordView.as_view(), name='change-password'),
	#
	# # Восстановление пароля
	# path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
              ]
