from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import PersonProfileView, SuggestCityView

urlpatterns = patterns(
    '',
    url(r'^profile/$', login_required(PersonProfileView.as_view()),
        name="update_profile"),
    url(r'^city/suggest/$', login_required(SuggestCityView.as_view()),
        name="suggest_city")

)
