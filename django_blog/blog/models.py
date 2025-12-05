from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""Create a model Post in blog/models.py with the following fields:
title: models.CharField(max_length=200)
content: models.TextField()
published_date: models.DateTimeField(auto_now_add=True)
author: models.ForeignKey to Django’s User model, with a relation to handle multiple posts by a single author.
Run the migrations to create the model in the database: bash python manage.py makemigrations blog python manage.py migrate"""

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete= models.CASCADE,related_name='author')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete= models.CASCADE,related_name='comment_post')
    author = models.ForeignKey(User,on_delete= models.CASCADE,related_name='comment_author')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content