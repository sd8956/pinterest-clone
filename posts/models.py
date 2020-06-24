from django.db import models
from django.contrib.auth.models import User
from boards.models import Board

# Create your models here.

class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.profile', on_delete=models.CASCADE)

    board = models.ForeignKey(Board, on_delete=models.SET_NULL, blank=True, null=True)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return 'Pin {} by @{}'.format(self.title, self.user.username)
