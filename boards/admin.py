"""Boards admin classes."""

# Django
from django.contrib import admin

# Models
from boards.models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    """Board admin"""

    list_display = ('pk', 'user', 'title')

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
        ('Board', {
            'fields': (
                ('title',),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )

    readonly_fields = ('created', 'modified',)
