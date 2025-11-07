from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
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