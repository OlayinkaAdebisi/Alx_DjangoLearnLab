from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import book_list
from django.views.generic import ListView
from .models import CustomUser
"""from django.views.generic import TemplateView

class HelloView(TemplateView):
    A class-based view rendering a template named 'hello.html'.
    template_name = 'hello.html'"""
"""Implement a class-based view that renders a template"""
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, function based view!")
class HelloView(TemplateView):
    template_name = 'hello.html'
def book_list_view(request):
    books = book_list.objects.all()  # this fetches all book records
    return render(request, 'office/book_list.html', {'book_list': books})
class img_view(ListView):
    model = CustomUser
    template_name = 'office/view.html'
    context_object_name = 'users'