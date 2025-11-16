from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager,BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
#custom manager here
class CustomUserManager(BaseUserManager):
    def create_user(self, username,email=None, profile_photo= None, date_of_birth=None, password=None):
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email=None, profile_photo=None, date_of_birth=None, password=None):
        if not date_of_birth:
            from datetime import date
            date_of_birth = date(2000, 1, 1)
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='product_images/', blank=True, null=True)

    objects = CustomUserManager()

class Post(models.Model):
    ...

    class Meta:
        permissions = [
            ("can_view", "Can view post"),
            ("can_create", "Can create post"),
            ("can_edit", "Can edit post"),
            ("can_delete", "Can delete post")
        ]