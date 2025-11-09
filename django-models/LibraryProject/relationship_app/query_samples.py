from .models import Book
from .models import Library
from .models import Librarian
books=Book.objects.filter(author=author_name)
books.all()
books=Library.objects.get(name=library_name)
books.all()
books=Librarian.objects.get(Library=library_name)
books.all()
