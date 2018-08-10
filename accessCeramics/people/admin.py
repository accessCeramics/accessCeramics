from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Artist

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Personal Information'), {
            'fields': ('given_name', 'family_name', 'additional_name',
                       ('birth_year', 'death_year'),
                       'website')
        }),
        (_('Description'), {
            'fields': ('statement', 'bio')
        })
    )
    ordering = ['family_name', 'given_name', 'additional_name']


admin.site.register(Artist, ArtistAdmin)
