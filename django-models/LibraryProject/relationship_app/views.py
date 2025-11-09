from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.decorators import permission_required 
from django.http import HttpResponseForbidden



# Create your views here.
"""Create a function-based view in relationship_app/views.py that lists all books stored in the database.
This view should render a simple text list of book titles and their authors."""
def funct_view(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'relationship_app/list_books.html',context)
class class_view(ListView):
    model=Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'Library.books'
class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def is_admin(user):
    if user.profile.role == 'Admin':
        return user.profile.role == 'Admin'
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_member(user):
    if user.profile.role == 'Member':
        return user.profile.role == 'Member'
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def is_librarian(user):
    if user.profile.role == 'Librarian':
        return user.profile.role == 'Librarian'
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@permission_required('relationship_app.can_add_book',raise_exception=True)
@permission_required('relationship_app.can_change_book', raise_exception=True)
@permission_required('relationship_app.can_delete_book', raise_exception=True)