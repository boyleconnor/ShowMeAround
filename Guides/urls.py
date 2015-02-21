from django.conf.urls import patterns, url
from Guides.views import ProfileUpdate, ProfileDetail, TourList, TourCreate

urlpatterns = patterns('',
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetail.as_view()),
    url(r'^profile/(?P<pk>\d+)/edit/$', ProfileUpdate.as_view(), name='profile.edit'),
    url(r'^$', TourList.as_view(), name='tour.list'),
    url(r'^tour/create/$', TourCreate.as_view(), name='tour.create'),
)