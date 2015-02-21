from ShowMeAround.models import Tour
from django.forms import ModelForm, Form, CharField, FloatField
from django.forms.widgets import HiddenInput, TextInput, Textarea
from django.utils.translation import ugettext as _

class TourSearchForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['address', 'latitude', 'longitude']
        widgets = {'address': TextInput(attrs={'class': 'form-control', 'placeholder' : _('Type an address here')}), 
        'latitude' : HiddenInput, 'longitude' : HiddenInput
        }