from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Argument
from .models import Debate

# Create your views here.
class DebateListView(View):
    template_name = 'debate/list.html'

    def get(self, request, **kwargs):
        context = {}
        debate = Debate.objects.get_or_404(pk=kwargs['pk'])
        context['debate'] = debate
        context['arguments'] = Argument.objects.filter(
                                 debate__title=debate.title)
