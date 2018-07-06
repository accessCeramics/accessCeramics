from django.contrib import admin

from .models import Material, Technique, Work, WorkType, PyrometricCone

class WorkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')
    fieldsets = (
        ('Basic Metadata', {
            'fields': ('title', ('creators', 'date'), ('created_at', 'modified_at'))
        }),
        ('Tags', {
            'fields': ('techniques', 'materials', 'work_types', 'pyrometric_cones')
        }),
        ('Measurements', {
            'fields': ('height', 'width', 'depth', 'firing_temperature',
                       'second_firing_temperature')
        }),
        ('Additional Metadata', {
            'fields': ('description',)
        })
    )
    search_fields = ['title', 'creators__last_name']
    autocomplete_fields = ['creators', 'techniques', 'materials', 'work_types',
                           'pyrometric_cones']
    list_filter = ('date', 'created_at', 'modified_at')


class TechniqueAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class MaterialAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class WorkTypeAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class PyrometricConeAdmin(admin.ModelAdmin):
    ordering = ['number']
    search_fields = ['number']


admin.site.register(Work, WorkAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(PyrometricCone, PyrometricConeAdmin)
