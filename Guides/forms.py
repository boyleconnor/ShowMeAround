from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from Guides.models import Tour, Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {'user': HiddenInput()}


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'