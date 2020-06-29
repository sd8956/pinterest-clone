"""Board views"""

# Django 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Model 
from boards.models import Board
from posts.models import Post

# Form 
from boards.forms import BoardForm


class CreateBoardView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'boards/new.html'
    form_class = BoardForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


class DetailPostView(LoginRequiredMixin, DetailView):
    """Detail a specific post"""

    template_name = 'boards/detail.html'
    model = Board
    context_object_name = 'board'
    queryset = Board.objects.all()

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        board = self.get_object()
        context['posts'] = Post.objects.filter(board=board).order_by('-created')
        return context