from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

class AboutPageView(TemplateView):
    template_name='pages/about.html'

class HomePageView(TemplateView):
    template_name='pages/home.html'