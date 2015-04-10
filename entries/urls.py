from django.conf.urls import url

from entries.views import EntryCreateView, EntryListView, EntryDetailView

urlpatterns = [

    url(r'^entry/(?P<pk>\d+)', EntryDetailView.as_view(), 
        name='entry_detail'),
    url(r'^list/', EntryListView.as_view(), name='entry_list'),
    url(r'^createentry/', EntryCreateView.as_view(), 
        name='entry_create'),
]
