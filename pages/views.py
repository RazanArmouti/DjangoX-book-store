from django.views.generic import TemplateView,ListView
from django.db import models
from .models import Book


class HomePageView(ListView):
    template_name = 'pages/home.html'
    model = Book



class AboutPageView(TemplateView):
    template_name = 'pages/about.html'