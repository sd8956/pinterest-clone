"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.ModelForm):
    """Sign up form."""


    class Meta:
        """Form settings."""

        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
    
    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()