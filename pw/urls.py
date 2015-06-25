from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
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
    url(r'^fingerpint', 'gallery.views.fingerprint'),
    url(r'^favicon.ico$', RedirectView.as_view(url='static/favicon.ico')),
    url(r'^$', 'gallery.views.projects'),
    #url(r'^projects/$', 'gallery.views.projects'),
    url(r'^([^/]+)/$', 'gallery.views.project'),
    url(r'^([^/]+)/([^/]+)/$', 'gallery.views.gallery_item'),
    url(r'^([^/]+)/([^/]+)/image/$', 'gallery.views.gallery_item_image'),

)