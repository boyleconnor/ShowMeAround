from Guides.forms import ProfileForm
from Guides.models import Tour, Profile
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.


class TourListView(ListView):
    model = Tour
    template_name = 'index.html'


class TourCreateView(CreateView):
    model = Tour

class ProfileCreate(CreateView):
    model = Profile
    template_name = 'profile/edit.html'
    form_class = ProfileForm

    def post(self, request, *args, **kwargs):
        self.request.form.user = self.request.user
        return super(ProfileCreate, self).post(request, *args, **kwargs)
