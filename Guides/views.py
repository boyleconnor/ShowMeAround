from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView, UpdateView
from Guides.forms import UserForm, TourForm, ReviewForm
from Guides.models import Tour, User, Review
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from ShowMeAround.settings import TIME_BEFORE


class TourList(ListView):
    model = Tour
    form_class = TourForm
    template_name = 'index.html'


class TourCreate(CreateView):
    model = Tour
    form_class = TourForm
    template_name = 'tour/edit.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_guide:
            raise PermissionDenied('Please become a registered tour guide before you can create a tour')
        return super(TourCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.guide = self.request.user
        return super(TourCreate, self).form_valid(form)


class TourDetail(DetailView):
    model = Tour
    template_name = 'tour/detail.html'

    def get_context_data(self, **kwargs):
        context = super(TourDetail, self).get_context_data(**kwargs)
        context['user_in_tour'] = self.request.user in self.object.tourists.all()
        context['still_time'] = timezone.now() < self.object.start_time
        context['tour_over'] = timezone.now() > self.object.end_time
        return context


def join_tour(request, pk):
    active_tour = Tour.objects.get(pk=pk)
    if request.method == 'POST':
        if timezone.now() > (active_tour.start_time-TIME_BEFORE):
            raise PermissionDenied('Too late to join this tour')
        if active_tour.tourists.count() >= active_tour.capacity:
            raise PermissionDenied('Sorry, this tour is at capacity')
        active_tour.tourists.add(request.user.id)
        active_tour.save()
        return redirect(active_tour)
    elif request.method == 'GET':
        return render(request, 'tour/join.html', {'tour': active_tour})


def leave_tour(request, pk):
    active_tour = Tour.objects.get(pk=pk)
    if request.method == 'POST':
        active_tour.tourists.remove(request.user)
        active_tour.save()
        return redirect('home')
    elif request.method == 'GET':
        return render(request, 'tour/leave.html', {'tour': active_tour})


class ProfileDetail(DetailView):
    model = User
    template_name = 'profile/detail.html'
    context_object_name = 'profile'


class ProfileUpdate(UpdateView):
    model = User
    template_name = 'profile/edit.html'
    form_class = UserForm

    def get_object(self, queryset=None):
        profile = super(ProfileUpdate, self).get_object(queryset)
        if profile == self.request.user:
            return profile
        else:
            raise PermissionDenied


class ReviewCreate(CreateView):
    model = Review
    template_name = 'review/edit.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super(ReviewCreate, self).get_context_data(**kwargs)
        context['subject'] = User.objects.get(id=self.kwargs['subject_pk'])
        return context

    def get_form(self, form_class):
        form = super(ReviewCreate, self).get_form(form_class)
        return form

    def form_valid(self, form):
        form.instance.author = User.objects.get(id=self.request.user.id)
        form.instance.subject = User.objects.get(id=self.kwargs['subject_pk'])
        return super(ReviewCreate, self).form_valid(form)


class ReviewDetail(DetailView):
    model = Review
    template_name = 'review/detail.html'
