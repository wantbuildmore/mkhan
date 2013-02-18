from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .models import Person, City
from .forms import PersonForm, CityForm

__all__ = ("PersonProfileView", "SuggestCityView")


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
        response = super(SuggestCityView, self).form_valid(form)
        messages.success(
            self.request,
            _("City suggestion have been added"))
        return response
