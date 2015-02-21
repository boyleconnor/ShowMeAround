from django.shortcuts import render
from Guides.models import Tour
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.

class TourListView(ListView):
	model = Tour
	template_name = 'index.html'

class TourCreateView(CreateView):
	model = Tour