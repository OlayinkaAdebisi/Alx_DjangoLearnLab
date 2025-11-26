from django.db import models
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
class Product(models.Model):
    name = models.CharField(max_length=20)
class Description(models.Model):
    about = models.TextField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
class book_list(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)