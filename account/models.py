from django.contrib.auth.models import User, PermissionsMixin
from django.db import models



class Profile(models.Model):
	USER_TYPE = (
		('doctor', 'Shifokor'),
		('mother', 'Ona'),
		('bride', 'Kelin'),
		('girl', "Qiz"),
		('guest', 'Foydalanuvchi'),
		('admin', 'Admin'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	phone = models.CharField(max_length=15, null=True, blank=False)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
	bio = models.TextField(blank=True)

	birthday = models.DateField(null=True, blank=True)
	user_type = models.CharField(choices=USER_TYPE, max_length=100, default='user')

	def __str__(self):
		return f"{self.user.username} Profile"


class Health(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)


class DocumentCategory(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Document(models.Model):
	category_id = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='documents/', null=True, blank=True)



