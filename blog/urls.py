from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from app.urls import urlpatterns as app_urls

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
