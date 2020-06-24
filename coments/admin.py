"""Coment admin classes."""

# Django
from django.contrib import admin

# Models
from coments.models import Coment

@admin.register(Coment)
class ComentAdmin(admin.ModelAdmin):
    """Coment admin"""

    list_display = ('pk', 'user', 'text')

    list_display_links = ('pk', 'user')

    search_fields = (
        'user__username',
        'user__email',
        'post__title',
    )

    list_filter = (
        'created',
    )

    fieldsets = (
        ('User',{
            'fields': (
                ('user', 'profile'),
            )
        }),
        ('Post', {
            'fields': (
                ('post',),
            )
        }),
        ('Coment', {
            'fields': (
                ('text',),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created',),
            )
        })
    )

    readonly_fields = ('created',)



