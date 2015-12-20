from django.conf.urls import include, url
from django.contrib import admin

from entries.views import EntryListView
from .views import AngularView

urlpatterns = [
    url(r'^$', EntryListView.as_view(), name='home'),
    url(r'^dev/$', AngularView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^debate/', include('debate.urls', namespace='debate')),
    url(r'^entries/', include('entries.urls', namespace='entries')),
]
