# home/urls.py

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # '' since it's the homepage
]
