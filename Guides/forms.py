from django.forms.models import ModelForm, ModelChoiceField
from django.forms.widgets import HiddenInput, TextInput
from Guides.models import Tour, User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['user', 'is_guide', 'profile_picture']
        widgets = {'name': TextInput()}

    def save(self, commit=True):
        return super()


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'