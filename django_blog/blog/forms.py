from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment

# add more files to the usercreationform
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
# allows user to edit the user profile 
class Update_User(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
# creates a form for user to create blog
class createpost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
# retrieve and allows user edit existing form
class updatepost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']

# form for the comment model
class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','content']