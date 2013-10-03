# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from gallery.models import Project, GalleryItem

def home (request):
    return render(request, 'home.html',)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    gallery_items = GalleryItem.objects.filter(project=project.id)
    return render(request, 'project.html', {'project': project, 'gallery_items': gallery_items,})

def gallery_item(request, project_id, gallery_item_id):
    project = Project.objects.get(pk=project_id)
    gallery_item = GalleryItem.objects.get(pk=gallery_item_id)
    return render(request, 'gallery_item.html', {'project': project, 'gallery_item': gallery_item,})
