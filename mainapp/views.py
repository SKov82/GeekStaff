from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Главная страница
    """    
    template_name = 'mainapp/index.html'
    extra_context = {'title_name': 'GeekStaff'}
    