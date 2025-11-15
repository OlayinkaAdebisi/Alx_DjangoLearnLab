from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, UserManager

#custom manager here
class CustomUserManager(UserManager):
    def create_user(self, username, profile_photo= None, date_of_birth=None, password=None):
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            username=username,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, profile_photo=None, date_of_birth=None, password=None):
        
        user = self.create_user(
            username,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), 
                                                     ('Librarian', 'Librarian'),
                                                       ('Member', 'Member')])
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='product_images/')
    objects = CustomUserManager()