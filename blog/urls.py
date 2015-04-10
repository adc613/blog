from django.conf.urls import include, url
from django.contrib import admin

from views import home

urlpatterns = [
    url(r'^$', home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^entries/', include('entries.urls', namespace='entries')),
]
