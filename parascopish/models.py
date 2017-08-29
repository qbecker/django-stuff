from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
import os


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    short_description = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='parascopish/static/')
    
    @property
    def filename(self):
        return os.path.basename(self.picture.name)
    
    def publush(self):
        self.publish_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    