from django.db import models

# Create your models here.
# the author model containing the author`s name
class Author(models.Model):
    name= models.CharField(max_length=40)

    def __str__(self):
        return self.name
# The book model containing title,publication_year and a foreign key(author)
class Book(models.Model):
    title = models.CharField(max_length=20)
    publication_year = models.IntegerField()
    #many books can belong to single author 
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year}) by {self.author}"