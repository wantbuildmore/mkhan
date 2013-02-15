from django import forms

from .models import Person


__all__ = ("PersonForm",)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            "name", "name_en",
            "email", "loc")
