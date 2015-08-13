from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list/(?P<pk>\d+)/$', views.DebateListView.as_view(), 
        name='list'),
]
