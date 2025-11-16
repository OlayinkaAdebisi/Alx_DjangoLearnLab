from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='library')
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library,  on_delete=models.CASCADE)
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), 
                                                     ('Librarian', 'Librarian'),
                                                       ('Member', 'Member')])
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()