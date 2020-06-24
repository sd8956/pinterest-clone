from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    """Board model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return 'Board {} by @{}'.format(self.title, self.user.username)

