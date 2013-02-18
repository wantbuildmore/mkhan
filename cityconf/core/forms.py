from django import forms

from .models import Person, City


__all__ = ("PersonForm", "CityForm")


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            "name", "name_en",
            "email", "loc", "company", "position")


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = (
            "country", "name", "name_en")
