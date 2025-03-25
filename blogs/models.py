from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='PB')


class PostCategory(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()


class Post(models.Model):
	STATUS = (
		('DF', 'Draft'),
		("PB", "Published"),
	)

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

	title = models.CharField(max_length=300)
	body = models.TextField()

	published_at = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	status = models.CharField(max_length=10, choices=STATUS, default='DF')

	objects = models.Manager()
	published = PublishedManager()

	class Meta:
		ordering = ('-publish',)
		indexes = [
			models.Index(fields=['-publish']),
		]

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post,
	                         on_delete=models.CASCADE,
	                         related_name="comments", )
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['created']
		indexes = [
			models.Index(fields=['created']),
		]

	def __str__(self):
		return f'Comment by {self.name} on {self.post}'
