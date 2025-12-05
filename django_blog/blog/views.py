from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
# Create your views here.
#Custom register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()  
    return render(request, 'blog/register.html', {'form': form})
# makes profile
@login_required
def profile(request):
    return render(request, 'blog/profile.html')
#To edit profile
@login_required
def edit_profile(request):
    user = request.user

    if request.method == "POST":
        form = Update_User(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = Update_User(instance=user)

    return render(request, 'blog/edit_profile.html', {'form': form})

# View for the blog Post model
class Postlistview(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'Post'

class Postdetailview(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'Post'
class PostCreateView (LoginRequiredMixin, CreateView):
    model = Post
    form_class = createpost
    template_name = "blog/create.html"
    context_object_name = 'Post-create'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = updatepost
    template_name = "blog/post_form.html"
    context_object_name = 'Post-update'
    success_url = reverse_lazy('list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete.html"
    success_url = reverse_lazy('list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context
        
class CommentList(ListView):
    model = Comment
    template_name = "blog/comment_list.html"
    context_object_name = 'Comment_list'
class CommentCreate(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = commentForm
    template_name = "blog/comment_create.html"
        

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('Comment_list', kwargs={'pk': self.kwargs['pk']})


class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = commentForm
    template_name = "blog/comment_list.html"
    success_url = reverse_lazy('Comment_list')

        
        
class CommentDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = ""
        #success_url = reverse_lazy('')

       