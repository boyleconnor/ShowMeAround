from django.conf.urls import patterns, url
from Guides.views import ProfileUpdate, ProfileDetail, TourList, TourCreate, leave_tour, join_tour, TourDetail

urlpatterns = patterns('',
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetail.as_view(), name='user.detail'),
    url(r'^profile/(?P<pk>\d+)/edit/$', ProfileUpdate.as_view(), name='user.edit'),
    url(r'^$', TourList.as_view(), name='tour.list'),
    url(r'^tour/create/$', TourCreate.as_view(), name='tour.create'),
    url(r'^tour/(?P<pk>\d+)/$', TourDetail.as_view(), name='tour.detail'),
    url(r'^tour/(?P<pk>\d+)/leave/$', leave_tour, name='tour.leave'),
    url(r'^tour/(?P<pk>\d+)/join/$', join_tour, name='tour.join'),
)