from django.views.generic import DetailView, UpdateView
from Guides.forms import UserForm, TourForm
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


class ProfileUpdate(UpdateView):
    model = User
    template_name = 'profile/edit.html'
    form_class = UserForm


def joinTour(request, tour_id, user_id):
    activeTour = Tour.objects.get(pk=tour_id)
    activeTour.tourists.add(User.objects.get(pk=user_id))
    activeTour.save()
    return render('index.html')

def leaveTour(request, tour_id, user_id):
    activeTour = Tour.objects.get(pk=tour_id)
    activeTour.tourists.remove(User.objects.get(pk=user_id))
    activeTour.save()
    return render('index.html')
