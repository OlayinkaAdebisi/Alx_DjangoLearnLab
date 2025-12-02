from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# You can define the class right here
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
# Create your views here.
#
def signup(request):
    return render(request,'blog/signup.html')
#@login_required
def profile(request):
    return render(request, 'blog/profile.html')