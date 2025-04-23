import dns.resolver
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
		read_only_fields = ('id', 'created_at', 'updated_at')


class CustomRegisterSerializer(RegisterSerializer):
	username = None  # Убираем username
	email = serializers.EmailField(required=True)

	def validate_email(self, email):
		"""Проверяем, есть ли уже такой email"""
		if User.objects.filter(email=email).exists():
			raise serializers.ValidationError("This email is already in use.")

		# 🧠 Проверка на существование MX-записи домена
		domain = email.split('@')[-1]
		try:
			dns.resolver.resolve(domain, 'MX')
		except dns.resolver.NXDOMAIN:
			raise serializers.ValidationError("Домен email не существует.")
		except dns.resolver.NoAnswer:
			raise serializers.ValidationError("У домена нет почтового сервера.")
		except dns.exception.Timeout:
			raise serializers.ValidationError("Проверка email заняла слишком много времени.")
		except Exception:
			raise serializers.ValidationError("Ошибка при проверке email.")

		return email

	def validate(self, attrs):
		attrs['username'] = attrs.get('email')  # Подменяем username на email
		return super().validate(attrs)


class CustomLoginSerializer(LoginSerializer):
	username = None  # Полностью убираем поле username
	email = serializers.EmailField(required=True)  # Делаем email обязательным

	def validate(self, attrs):
		attrs['username'] = attrs.get('email')  # Чтобы обойти внутреннюю валидацию
		return super().validate(attrs)


class CustomTokenSerializer(serializers.Serializer):
	access = serializers.CharField()
	refresh = serializers.CharField()

	def to_representation(self, instance):
		"""
		Переопределяем метод, чтобы refresh-токен добавлялся
		"""
		refresh = RefreshToken.for_user(self.context['user'])  # Генерируем refresh-токен
		return {
			"access": str(refresh.access_token),
			"refresh": str(refresh),
		}
