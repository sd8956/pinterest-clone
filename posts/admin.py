"""Posts admin classes."""

# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts admin"""

    list_display = ('pk', 'user', 'title', 'photo')

    list_display_links = ('pk', 'user', 'title')

    search_fields = (
        'user__username',
        'user__email',
        'title',
    )

    list_filter = (
        'created',
        'modified',
    )

    fieldsets = (
        ('User', {
            'fields': (
                ('user', 'profile'),
            )
        }),
        ('Post', {
            'fields': (
                ('title',),
                ('photo',),
            )
        }),
        ('Board', {
            'fields': (
                ('board',),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )

    readonly_fields = ('created', 'modified',)
