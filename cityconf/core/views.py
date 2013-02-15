from django.views.generic.edit import CreateView

from .models import Person
from .forms import PersonForm

__all__ = ("PersonProfileView",)


class PersonProfileView(CreateView):
    template_name = "core/profile.html"
    form_class = PersonForm
    model = Person
    # TODO: use ``url_for`` ?
    success_url = '/profile/updated/'

    def form_valid(self, form):
        # form.send_email()
        return super(PersonProfileView, self).form_valid(form)
