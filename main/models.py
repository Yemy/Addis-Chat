from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# models here.

# message
# notification
# like
# comment
# post
# follow
# 

class Posts(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=500, blank=True, null=True)
	image = models.ImageField(upload_to='attachments', blank=True, null=True)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = "Posts"
