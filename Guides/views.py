from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView, UpdateView
from Guides.forms import ProfileForm, TourForm, ReviewForm
from Guides.models import Tour, User, Review
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from ShowMeAround.settings import TIME_BEFORE
