from django.views.generic import DetailView, UpdateView
from Guides.forms import ProfileForm
from Guides.models import Profile


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile/detail.html'
    context_object_name = 'profile'


class ProfileUpdate(UpdateView):
    model = Profile
    template_name = 'profile/edit.html'
    form_class = ProfileForm