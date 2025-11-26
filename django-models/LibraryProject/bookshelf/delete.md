#to get and delete
from bookshelf.models import Book
book = Book.objects.all()
book.delete()
books = Book.objects.all()
