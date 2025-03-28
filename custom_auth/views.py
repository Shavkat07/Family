from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, CustomUserSerializer, \
	SetNewPasswordSerializer, ChangePasswordSerializer, ResetPasswordSerializer, LogoutSerializer
from rest_framework import viewsets


class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = (AllowAny,)


class CustomTokenObtainPairView(generics.GenericAPIView):
	serializer_class = CustomTokenObtainPairSerializer
	permission_classes = (AllowAny,)

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		return Response(serializer.validated_data, status=status.HTTP_200_OK)


class LogoutView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request):
		serializer = LogoutSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		try:
			refresh_token = serializer.validated_data["refresh"]
			token = RefreshToken(refresh_token)
			token.blacklist()  # Добавляем токен в черный список
			return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileUserView(generics.RetrieveAPIView):
	permission_classes = [IsAuthenticated]
	queryset = User.objects.all()
	serializer_class = CustomUserSerializer

	def get_object(self):
		return self.request.user


class UserViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	queryset = User.objects.all()
	serializer_class = CustomUserSerializer


# Password Views

class SetNewPasswordView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request):
		serializer = SetNewPasswordSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(request.user)
			return Response({"detail": "Password has been updated successfully."}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
	permission_classes = [IsAuthenticated]  # Требует авторизации

	def post(self, request):
		serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			request.user.set_password(serializer.validated_data['new_password'])
			request.user.save()
			return Response({"detail": "Password changed successfully."}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
	def post(self, request):
		serializer = ResetPasswordSerializer(data=request.data)
		if serializer.is_valid():
			email = serializer.validated_data['email']
			user = User.objects.filter(email=email).first()
			if user:
				# Здесь отправка email с токеном восстановления (пример)
				return Response({"detail": "Password reset link sent to your email."}, status=status.HTTP_200_OK)
			return Response({"error": "User with this email not found."}, status=status.HTTP_404_NOT_FOUND)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
