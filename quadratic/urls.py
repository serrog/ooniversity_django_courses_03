from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
	url(r'^results/(?P<a>-?\w*)/(?P<b>-?\w*)/(?P<c>-?\w*)/$', views.quadratic_results, name='results'),
)