from django.conf.urls import patterns, url
from Guides.views import ProfileUpdate, ProfileDetail, TourList, TourCreate, leaveTour, joinTour

urlpatterns = patterns('',
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetail.as_view(), name='user.detail'),
    url(r'^profile/(?P<pk>\d+)/edit/$', ProfileUpdate.as_view(), name='user.edit'),
    url(r'^$', TourList.as_view(), name='tour.list'),
    url(r'^tour/create/$', TourCreate.as_view(), name='tour.create'),
    url(r'^tour/leave/(\d+)/(\d+)', leaveTour, name='tour.leave'),
    url(r'^tour/join/(\d+)/(\d+)', joinTour, name='tour.join'),
)