
# Django
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('', include(('boards.urls', 'boards'), namespace='boards'))
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
