from django.shortcuts import render
from django.views import generic

from .models import Pin, Tag


class IndexListView(generic.ListView):
    model = Pin
    template_name = 'pinboard/index.html'
    paginate_by = 12


class PinDetailView(generic.DetailView):
    model = Pin
    template_name = 'pinboard/pin_detail.html'
