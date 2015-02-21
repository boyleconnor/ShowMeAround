from django.contrib.auth.models import User
from django.forms.models import ModelForm, ModelChoiceField
from django.forms.widgets import HiddenInput, TextInput
from Guides.models import Tour, Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'is_guide']
        widgets = {'name': TextInput()}
    user = ModelChoiceField(widget=HiddenInput(), queryset=User.objects.all(), required=False)


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'