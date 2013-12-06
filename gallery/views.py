# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from gallery.models import Project, GalleryItem

import operator

def home(request):
    return render(request, 'home.html',)

def projects(request):
    projects = Project.objects.all()
    projects_sorted = sorted(projects, key=operator.attrgetter('rank'))
    return render(request, 'projects.html', {'projects': projects_sorted})

def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    gallery_items = GalleryItem.objects.filter(project=project.id)
    gallery_items_sorted = sorted(gallery_items, key=operator.attrgetter('rank'))
    # Single gallery item projects go straight to galery item.
    if len(gallery_items) == 1:
        gallery_item_id = gallery_items_sorted[0].id
        return HttpResponseRedirect(reverse('gallery.views.gallery_item', args=[project_id, gallery_item_id,]))
    # Multiple gallery item or empty projects go to list of gallery items.
    else:
        return render(request, 'project.html', {'project': project, 'gallery_items': gallery_items_sorted,})

def gallery_item(request, project_id, gallery_item_id):
    project = Project.objects.get(pk=project_id)
    gallery_item = GalleryItem.objects.get(pk=gallery_item_id)
    media_type = str(gallery_item.media_type)
    if media_type == "Internet":
        url = gallery_item.url
    else:
        url = ''
    return render(request, 'gallery_item.html', {'project': project, 'gallery_item': gallery_item, 'media_type': media_type, 'url': url,})


def gallery_item_image(request, project_id, gallery_item_id):
    project = Project.objects.get(pk=project_id)
    gallery_item = GalleryItem.objects.get(pk=gallery_item_id)
    return render(request, 'gallery_item_image.html', {'project': project, 'gallery_item': gallery_item,})