from django.shortcuts import render

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, FormView, UpdateView, CreateView, DetailView
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post
from boards.models import Board

# Forms 
from users.forms import SignupForm


def SignupView(request):
    if request.method == 'POST':

        username = request.POST['username']
        passdw = request.POST['password']
        passwd_co = request.POST['password_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if passdw != passwd_co:
            return render(request, 'users/singup.html', {'error': 'Password confirmation does not mach'})
        
        user = User.objects.create_user(username=username, password=passdw)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        profile = Profile(user=user)
        profile.save()

        return redirect('users:login')

    return render(request, 'users/singup.html')


class LoginView(auth_views.LoginView):
    """Login view"""

    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['board'] = True
        context['pin'] = None
        context['boards'] = Board.objects.filter(user=user).order_by('-created')
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class UserDetailViewPins(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['pin'] = True
        context['board'] = None
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['biography','picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})