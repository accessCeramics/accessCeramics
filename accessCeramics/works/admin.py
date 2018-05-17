from django.contrib import admin

from .models import Material, Technique, Work, WorkType, Temperature

class WorkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')
    fieldsets = (
        ('Basic Metadata', {
            'fields': ('title', ('creators', 'date'), ('created_at', 'modified_at'))
        }),
        ('Tags', {
            'fields': ('techniques', 'materials', 'work_types', 'temperatures')
        }),
        ('Dimensions', {
            'fields': ('height', 'width', 'depth')
        }),
        ('Additional Metadata', {
            'fields': ('description', 'credits')
        })
    )
    search_fields = ['title', 'creators__last_name']
    autocomplete_fields = ['creators', 'techniques', 'materials', 'work_types', 'temperatures']
    list_filter = ('creators__last_name', 'date')


class TechniqueAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

    
class MaterialAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class WorkTypeAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class TemperatureAdmin(admin.ModelAdmin):
    ordering = ['value']
    search_fields = ['value']


admin.site.register(Work, WorkAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(Temperature, TemperatureAdmin)