from django.contrib import admin

from works.models import Material, Technique, Work, WorkType

class WorkAdmin(admin.ModelAdmin):
    pass

class TechniqueAdmin(admin.ModelAdmin):
    pass
    
class MaterialAdmin(admin.ModelAdmin):
    pass

class WorkTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Work, WorkAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(WorkType, WorkTypeAdmin)