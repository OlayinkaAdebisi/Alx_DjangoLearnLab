from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
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
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='product_images/')
    objects = CustomUserManager()