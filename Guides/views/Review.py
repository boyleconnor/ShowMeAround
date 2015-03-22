from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView
from Guides.forms import ReviewForm
from Guides.models import Review


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