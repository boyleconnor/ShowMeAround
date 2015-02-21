from django.forms.models import ModelForm, ModelChoiceField
from django.forms.widgets import HiddenInput, TextInput
from Guides.models import Tour, User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {'name': TextInput()}


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'