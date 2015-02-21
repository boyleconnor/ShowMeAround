from datetimewidget.widgets import DateTimeWidget
from django.forms.models import ModelForm, ModelChoiceField
from django.forms.widgets import HiddenInput, TextInput
from Guides.models import Tour, User, Review


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'languages']
        widgets = {'name': TextInput()}


class TourForm(ModelForm):
    class Meta:
        model = Tour
        exclude = ['guide', 'tourists']
        widgets = {
            'start_time': DateTimeWidget(usel10n=True, bootstrap_version=3),
            'end_time': DateTimeWidget(usel10n=True, bootstrap_version=3),
            'title': TextInput(),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'subject']
        widgets = {
            'tour': HiddenInput(),
        }