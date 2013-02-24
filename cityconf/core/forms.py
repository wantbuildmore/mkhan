from django import forms

from .models import Person, City, Conference


__all__ = ("PersonForm", "CityForm", "ConferenceForm")


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


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = (
            "title", "title_en",
            "location", "date")
