from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pw.views.home', name='home'),
    # url(r'^pw/', include('pw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gallery.views.home'),
    url(r'^projects/$', 'gallery.views.projects'),
    url(r'^projects/(\d+)/$', 'gallery.views.project'),
    url(r'^projects/(\d+)/(\d+)/$', 'gallery.views.gallery_item')
)