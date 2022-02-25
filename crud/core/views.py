from django.shortcuts import render
from django.views.generic.base import TemplateView



class HomePageView (TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Homes'
        return context

class SamplePageView (TemplateView):

    template_name = "core/sample.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Home Pages'
        return context


