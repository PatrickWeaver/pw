# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from gallery.models import Project, GalleryItem, ExternalLink

import operator

def home(request):
    return render(request, 'home.html',)

def projects(request):
    projects = Project.objects.all()
    external_links = ExternalLink.objects.all()

    projects_sorted = sorted(projects, key=operator.attrgetter('rank'))
    external_links_sorted = sorted(external_links, key=operator.attrgetter('rank'))

    return render(request, 'projects.html', {'projects': projects_sorted, 'external_links': external_links_sorted,})

def project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    gallery_items = GalleryItem.objects.filter(project=project.id)
    gallery_items_sorted = sorted(gallery_items, key=operator.attrgetter('rank'))
    # Single gallery item projects go straight to galery item.
    if len(gallery_items) == 1:
        gallery_item_slug = gallery_items_sorted[0].slug
        return HttpResponseRedirect(reverse('gallery.views.gallery_item', args=[project_slug, gallery_item_slug,]))
    # Multiple gallery item or empty projects go to list of gallery items.
    else:
        return render(request, 'project.html', {'project': project, 'gallery_items': gallery_items_sorted,})

def gallery_item(request, project_slug, gallery_item_slug):
    project = Project.objects.get(slug=project_slug)
    gallery_item = GalleryItem.objects.get(slug=gallery_item_slug)
    media_type = str(gallery_item.media_type)
    if media_type == "Internet":
        url = gallery_item.url
    else:
        url = ''
    return render(request, 'gallery_item.html', {'project': project, 'gallery_item': gallery_item, 'media_type': media_type, 'url': url,})


def gallery_item_image(request, project_slug, gallery_item_slug):
    project = Project.objects.get(slug=project_slug)
    gallery_item = GalleryItem.objects.get(slug=gallery_item_slug)
    return render(request, 'gallery_item_image.html', {'project': project, 'gallery_item': gallery_item,})

def fingerprint():
    return render(request, 'fingerprint.html')