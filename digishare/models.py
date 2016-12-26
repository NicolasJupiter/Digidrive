from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# from django.urls import reverse

# Create your models here.
class _video(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    video_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    video_path = models.CharField(max_length=200, blank=True, null=True)

    # def get_absolute_url(self):
    #     return reverse('next', kwargs={'pk': self.pk})

class Site_user(models.Model):

    su_student = models.OneToOneField(User)