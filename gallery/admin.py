from django.contrib import admin
from gallery.models import GalleryItem, Project, ExternalLink

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class GalleryItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)
admin.site.register(ExternalLink)