# home/views.py

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'public/home.html'  # assuming home.html is the name of your template
