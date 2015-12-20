from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'blog/home.html'


class AngularView(TemplateView):
    template_name = 'index.html'
