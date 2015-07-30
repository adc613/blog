from django.conf.urls import include, url
from django.contrib import admin

from entries.views import EntryListView

urlpatterns = [
    url(r'^$', EntryListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^entries/', include('entries.urls', namespace='entries')),
]

