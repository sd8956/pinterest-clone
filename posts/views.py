"""Post views"""

# Django 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Models
from posts.models import Post
from boards.models import Board

# Forms 
from posts.forms import PostForm, PostBoardForm

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    context_object_name = 'posts'


class DetailPostView(LoginRequiredMixin, DetailView):
    """Detail a specific post"""

    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


class CreatePostBoardView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostBoardForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and board to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        context['board'] = self.request.GET.get('board')
        return context
