from django.conf.urls import include, url

from rest_framework import routers

from entries import views

router = routers.DefaultRouter()
router.register(r'entries', views.EntryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'a/', views.AngularView.as_view(), name='angular'),
    url(r'^entry/(?P<pk>\d+)', views.EntryDetailView.as_view(),
        name='entry_detail'),
    url(r'^list/', views.EntryListView.as_view(), name='entry_list'),
    url(r'^createentry/', views.EntryCreateView.as_view(),
        name='entry_create'),
]
