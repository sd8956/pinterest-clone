"""Post forms."""

# Django
from django import forms

# Models
from boards.models import Board


class BoardForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Board
        fields = ('user', 'profile', 'title')
    

