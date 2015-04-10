from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Entry
from .forms import EntryCreationForm

# Create your views here.
class EntryListView(ListView):
    model = Entry

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(View):
    template_name='entries/entry_create.html'
    form = EntryCreationForm

    @method_decorator(login_required)
    def get(self,request):
        return render(request, self.template_name, {'form' : form})

    @method_decorator(login_required)
    def post(self, request):
        if form.is_valid():
            entry = form.save(commit=False)
            entry.creator = request.user
            entry.save()

        return HttpResponseRedirect(reverse('home'))
