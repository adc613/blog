from django.forms import ModelForm

from .models import Entry

class EntryCreationForm(ModelForm):

    class Meta:
        model = Entry
        fields = ['article', 'title']
