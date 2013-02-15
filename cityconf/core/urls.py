from django.conf.urls import patterns, url

from .views import PersonProfileView

urlpatterns = patterns(
    '',
    url(r'^profile/$', PersonProfileView.as_view()),
)
