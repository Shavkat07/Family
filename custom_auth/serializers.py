from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
		'id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'createdAt', 'updatedAt')
		read_only_fields = ('id', 'createdAt', 'updatedAt')


class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ('id', 'email', 'first_name', 'last_name', 'password')

	def create(self, validated_data):
		user = User.objects.create_user(
			email=validated_data['email'],
			password=validated_data['password'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
		)
		return user


class CustomTokenObtainPairSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(write_only=True)

	def validate(self, attrs):
		email = attrs.get('email')
		password = attrs.get('password')

		user = authenticate(username=email, password=password)
		if user is None:
			raise serializers.ValidationError('Invalid credentials')

		refresh = RefreshToken.for_user(user)
		return {
			'refresh': str(refresh),
			'access': str(refresh.access_token),
			'user_data': CustomUserSerializer(user).data
		}


class LogoutSerializer(serializers.Serializer):
	refresh = serializers.CharField()


class SetNewPasswordSerializer(serializers.Serializer):
	user_id = serializers.IntegerField()  # User ID or any identifier you use
	new_password = serializers.CharField(write_only=True, required=True)

	def validate_new_password(self, value):
		try:
			validate_password(value)  # Проверка сложности пароля
		except ValidationError as e:
			raise serializers.ValidationError(e.messages)
		return value

	def validate_user_id(self, value):
		try:
			user = User.objects.get(pk=value)
		except User.DoesNotExist:
			raise serializers.ValidationError("User does not exist.")
		return value

	def save(self, user):
		# user_id = self.validated_data['user_id']
		new_password = self.validated_data['new_password']

		# user = User.objects.get(pk=user_id)
		user.set_password(new_password)
		user.save()


class ChangePasswordSerializer(serializers.Serializer):
	old_password = serializers.CharField(write_only=True, required=True)
	new_password = serializers.CharField(write_only=True, required=True)

	def validate_old_password(self, value):
		user = self.context['request'].user
		if not user.check_password(value):
			raise serializers.ValidationError("Old password is incorrect.")
		return value


class ResetPasswordSerializer(serializers.Serializer):
	email = serializers.EmailField()
