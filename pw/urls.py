from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import re

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pw.views.home', name='home'),
    # url(r'^pw/', include('pw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gallery.views.projects'),
    #url(r'^projects/$', 'gallery.views.projects'),
    url(r'^projects/([^/]+)/$', 'gallery.views.project'),
    url(r'^projects/([^/]+)/([^/]+)/$', 'gallery.views.gallery_item'),
    url(r'^projects/([^/]+)/([^/]+)/image/$', 'gallery.views.gallery_item_image'),
)