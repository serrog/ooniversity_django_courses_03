from django.conf.urls import patterns, url

from coaches import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.CoachDetailView.as_view(), name='detail'),
)