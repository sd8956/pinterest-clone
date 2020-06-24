from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Coment(models.Model):
    """Coment model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.profile', on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    text = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the coment text and user"""
        return '{} by @{}'.format(self.text, self.user.username)
        