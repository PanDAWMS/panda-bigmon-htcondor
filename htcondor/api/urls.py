from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('api.views',
    url(r'^jobs/$', views.JobList.as_view()),
    url(r'^jobs/(?P<pk>\S+)$', views.JobDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
