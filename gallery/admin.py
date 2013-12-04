from django.contrib import admin
from gallery.models import GalleryItem, Project


admin.site.register(Project)
admin.site.register(GalleryItem)
