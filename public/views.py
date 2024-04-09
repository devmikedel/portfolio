# home/views.py

from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'public/home.html'  # assuming home.html is the name of your template


class ToolsView(TemplateView):  # Define a new class based view
    template_name = 'public/tools.html'