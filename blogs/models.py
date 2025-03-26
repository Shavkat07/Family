from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='PB')


class PostCategory(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True ,blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	STATUS = (
		('DF', 'Draft'),
		("PB", "Published"),
	)

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

	title = models.CharField(max_length=300,)
	body = models.TextField()

	published_at = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(auto_now_add=True )
	updated_at = models.DateTimeField(auto_now=True)

	status = models.CharField(max_length=10, choices=STATUS, default='DF')

	objects = models.Manager()
	published = PublishedManager()

	class Meta:
		ordering = ('-published_at',)
		indexes = [
			models.Index(fields=['-published_at']),
		]

	def __str__(self):
		return self.title

class PostImage(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='media/images/post_images/')
	caption = models.CharField(max_length=255, blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Image for ({self.post}) "


class Comment(models.Model):
	post = models.ForeignKey(Post,
	                         on_delete=models.CASCADE,
	                         related_name="comments", )
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['created_at']
		indexes = [
			models.Index(fields=['created_at']),
		]

	def __str__(self):
		return f'Comment by ({self.name}) on ({self.post})'
