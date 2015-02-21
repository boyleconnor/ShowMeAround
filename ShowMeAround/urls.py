from django.conf.urls import *
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('guides:tour.list'))),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^guides/', include('Guides.urls', namespace='guides')),
)

