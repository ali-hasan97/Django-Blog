from unicodedata import category
from django import forms
from django.shortcuts import render
from . models import Post, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . forms import PostForm, UpdateForm
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.

""" 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
"""

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__name=cats)
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'cats':cats, 'category_posts':category_posts, 'categories':categories})
    

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'blog/category_form.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostCreateView(LoginRequiredMixin, CreateView): #login reqd makes sure user is logged in
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #userpasssestest makes sure only the correct user can change their own stuff.
    model = Post
    form_class = UpdateForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #userpassestest required this func to make sure users arent changing other users' blogs.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): #userpassestest required this func to make sure users arent changing other users' blogs.
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

# blog/post_list.html
# <app>/<model>_<viewtype>.html is the naming convention.

# class AboutView(ListView):
    # template_name = 'blog/about.html'

def about(request):
    categories = Category.objects.all()
    return render(request, 'blog/about.html', {'title': 'About', 'categories': categories})