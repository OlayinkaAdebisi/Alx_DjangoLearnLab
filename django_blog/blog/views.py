from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    UserRegisterForm, 
    Update_User, 
    createpost, 
    updatepost, 
    CommentForm
)

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
        
class CommentCreateView(ListView):
    model = Comment
    template_name = "blog/comment_list.html"
    context_object_name = 'Comment_list'

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'])
class CommentCreate(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_create.html"
        

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('Comment_list', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_create.html"
    success_url = reverse_lazy('Comment_list')
    context_object_name = 'comment_update'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

        
        
class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = "blog/delete.html"
    
    
    def get_success_url(self):
        post_id = self.object.post.pk
        return reverse('Comment_list', kwargs={'pk': post_id})
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

       