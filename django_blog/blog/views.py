from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# You can define the class right here
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
# Create your views here.
#
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  # Use the custom form here
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()  # Use the custom form here too
    return render(request, 'blog/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'blog/profile.html')
#f
