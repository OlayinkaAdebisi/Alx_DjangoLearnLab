from .models import Book
from .models import Library
from .models import Librarian
books=Author.objects.get(name=author_name)
books.objects.filter(author=author)
books=Library.objects.get(name=library_name)
books.all()
books=Librarian.objects.get(library=li)
books.all()
