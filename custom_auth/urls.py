from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, ProfileUserView, UserViewSet, SetNewPasswordView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
] + router.urls

