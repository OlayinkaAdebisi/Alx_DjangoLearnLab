from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import CustomUser, Book
from django.shortcuts import render, redirect
from .forms import ExampleForm
# Create your views here.
#it handles viewing
@permission_required('bookshelf.can_view', raise_exception=True)
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, "bookshelf/user_list.html", {"users": users})
#it handles creating post
@permission_required('bookshelf.can_create', raise_exception=True)
def create_user(request):
    if request.method == "POST":
        return redirect("user_list")
    return render(request, "bookshelf/create_user.html")
#it handles editing
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        user.save()
        return redirect("user_list")
    return render(request, "bookshelf/edit_user.html", {"user": user})
#it handles deleting postd
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect("user_list")
#book_list
# views.py


def example_view(request):
   
    form = ExampleForm(request.POST or None)
    submitted_data = None

    if request.method == 'POST':
        if form.is_valid(): 
            submitted_data = form.cleaned_data['example_field']
            return render(request, 'form_example.html', {'form': form, 'submitted_data': submitted_data})
    
    return render(request, 'form_example.html', {'form': form, 'submitted_data': submitted_data})
