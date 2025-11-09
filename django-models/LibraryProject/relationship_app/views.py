from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView
# Create your views here.
"""Create a function-based view in relationship_app/views.py that lists all books stored in the database.
This view should render a simple text list of book titles and their authors."""
def funct_view(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'relationship_app/list_books.html',context)
class class_view(ListView):
    model=Library
    template_name = 'library_detail.html'
    context_object_name = 'relationship_app/Library.books'