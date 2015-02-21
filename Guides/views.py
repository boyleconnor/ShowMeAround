from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import DetailView
from Guides.forms import ProfileForm, TourForm
from Guides.models import Tour, User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.


class TourList(ListView):
    model = Tour
    form_class = TourForm
    template_name = 'index.html'


class TourCreate(CreateView):
    model = Tour
    form_class = TourForm


class TourDetail(DetailView):
    model = Tour
    template_name = 'tour/detail.html'


class ProfileDetail(DetailView):
    model = User
    template_name = 'profile/detail.html'


class ProfileUpdate(CreateView):
    model = User
    template_name = 'profile/edit.html'
    form_class = ProfileForm

    def dispatch(self, request, *args, **kwargs):
        try:
            request.user.profile
        except Exception:
            profile = User.objects.create(user=request.user)
            return redirect(profile.get_update_url())
        return super(ProfileUpdate, self).dispatch(request, *args, **kwargs)

