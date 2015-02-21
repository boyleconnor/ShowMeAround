from django.conf.urls import *

from django.contrib import admin
from django.views.generic import TemplateView
from Guides.views import TourListView, TourCreateView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TourListView.as_view(), name='tour-list'),
    url(r'^tours/create$', TourCreateView.as_view(), name="tour-create" ),
)
