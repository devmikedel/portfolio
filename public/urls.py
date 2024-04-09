# home/urls.py

from django.urls import path
from .views import HomePageView, ToolsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # '' since it's the homepage
    path('tools/', ToolsView.as_view(), name='tools'),
]
