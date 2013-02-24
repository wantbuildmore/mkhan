from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import PersonProfileView, SuggestCityView, CreateConferenceView, \
    ConferencesListView, CitiesListView, DeleteCityView, \
    DeleteConferenceView, ConferenceView


urlpatterns = patterns(
    '',
    # hanle conference-by-PK
    url(r'^conference/(?P<pk>[\d]+)/$',
        ConferenceView.as_view(),
        name="conference_pk"),
    # handle conference-by-slug
    url(r'^conference/(?P<slug>[A-Za-z0-9\-]+)/$',
        ConferenceView.as_view(),
        name="conference_slug"),
    url(r'^profile/$',
        login_required(PersonProfileView.as_view()),
        name="update_profile"),
    url(r'^cities/$',
        login_required(CitiesListView.as_view()),
        name="cities"),
    url(r'^city/suggest/$',
        login_required(SuggestCityView.as_view()),
        name="suggest_city"),
    url(r'^city/delete/(?P<pk>[\d]+)/$',
        login_required(DeleteCityView.as_view()),
        name="delete_city"),
    url(r'^conferencs/$',
        login_required(ConferencesListView.as_view()),
        name="conferences"),
    url(r'^conferences/create/$',
        login_required(CreateConferenceView.as_view()),
        name="create_conference"),
    url(r'^conferences/delete/(?P<pk>[\d]+)/$',
        login_required(DeleteConferenceView.as_view()),
        name="delete_conference"),
)
