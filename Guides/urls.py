from django.conf.urls import patterns, url
from Guides.views import ProfileCreate

urlpatterns = patterns('',
    url(r'profile/create/$', ProfileCreate.as_view()),
)
