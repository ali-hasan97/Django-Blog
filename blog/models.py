from pydoc_data.topics import topics
from unicodedata import category
from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_home')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,max_length=60, on_delete=models.CASCADE, related_name= 'category')
    # category = models.CharField(max_length=50, default='General')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})