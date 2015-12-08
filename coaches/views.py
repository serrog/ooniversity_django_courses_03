from django.shortcuts import render
from django.views.generic.detail import DetailView 
from coaches.models import Coach


class MixinCoachTitle(object):
    def get_context_data(self, **kwargs):
        context = super(MixinCoachTitle, self).get_context_data(**kwargs)
        context['title'] = "About coach"
        return context


class CoachDetailView(MixinCoachTitle, DetailView):
    model = Coach
    template_name = "coaches/detail.html"