from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import AngularView
from blog import settings
from entries.views import EntryListView

urlpatterns = [
    url(r'^old/$', EntryListView.as_view(), name='home'),
    url(r'^$', AngularView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^debate/', include('debate.urls', namespace='debate')),
    url(r'^entries/', include('entries.urls', namespace='entries')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
