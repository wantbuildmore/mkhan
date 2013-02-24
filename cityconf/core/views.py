from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .models import Person, City, Conference
from .forms import PersonForm, CityForm, ConferenceForm

__all__ = ("PersonProfileView", "SuggestCityView",
           "CreateConferenceView", "ConferencesListView",
           "CitiesListView", "DeleteConferenceView")


class PersonProfileView(UpdateView):
    template_name = "core/profile.html"
    form_class = PersonForm
    model = Person

    get_success_url = lambda s: reverse("update_profile")

    def get_object(self):
        obj, created = Person.objects.get_or_create(
            user=self.request.user)
        self.pk = obj.pk
        return obj

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()

        return HttpResponseRedirect(self.get_success_url())


class SuggestCityView(CreateView):
    template_name = "core/suggest_city.html"
    form_class = CityForm
    model = City

    get_success_url = lambda s: reverse("suggest_city")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.suggested_by = self.request.user
        instance.save()

        messages.success(
            self.request,
            _("City suggestion have been added"))

        return HttpResponseRedirect(self.get_success_url())


class CitiesListView(ListView):
    template_name = "core/cities.html"
    model = City

    def get_queryset(self):
        return City.objects.suggested_by(self.request.user)


class DeleteCityView(DeleteView):
    model = City

    template_name = "core/sys/confirm_delete.html"

    success_message = _("City deleted Successfully")
    get_success_url = lambda s: reverse("cities")

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteCityView, self).get_object()

        if (not obj.suggested_by == self.request.user or
                obj.is_verified is True):
            raise HttpResponseForbidden

        return obj


class CreateConferenceView(CreateView):
    template_name = "core/create_conference.html"

    form_class = ConferenceForm
    model = Conference

    get_success_url = lambda s: reverse("conferences")

    def form_valid(self, form):
        instance = form.save(commit=False)

        person = self.request.user.person_set.all()[0]
        instance.chairman = person

        instance.owner = self.request.user
        instance.save()

        messages.success(
            self.request,
            _("Conference suggestion have been added"))

        return HttpResponseRedirect(self.get_success_url())


class ConferencesListView(ListView):
    template_name = "core/conferences.html"
    model = Conference

    def get_queryset(self):
        return Conference.objects.owned_by(self.request.user)


class DeleteConferenceView(DeleteView):
    model = Conference

    template_name = "core/sys/confirm_delete.html"

    success_message = _("Conference deleted Successfully")
    get_success_url = lambda s: reverse("conferences")

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteConferenceView, self).get_object()

        if not obj.owner == self.request.user:
            raise HttpResponseForbidden

        return obj
