from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework import viewsets

from .models import Entry
from .forms import EntryCreationForm
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class AngularView(View):
    template_name = 'blog/angular_home.html'

    def get(self, request):
        return render(request, self.template_name, {})


class EntryListView(ListView):
    model = Entry
    template_name = "blog/home.html"

    def get_queryset(self):
        return self.model.objects.order_by('-creation_date')


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(View):
    template_name = 'entries/entry_create.html'
    form = EntryCreationForm

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    @method_decorator(login_required)
    def post(self, request):
        form = EntryCreationForm(request.POST)
        user = request.user
        if form.is_valid():
            entry = form.save(commit=False)
            entry.creator = user
            entry.save()

        return HttpResponseRedirect(reverse('home'))
