from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleCrud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'crud.views.index', name='index'),
    url(r'^insert$', 'crud.views.inset', name='inset'),
    url(r'^delete/(?P<person_id>\d+)$', 'crud.views.delete', name='delete'),
    url(r'^edit/(?P<person_id>\d+)$', 'crud.views.edit', name='edit'),


)
