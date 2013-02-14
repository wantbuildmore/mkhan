from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from composite_field import CompositeField
from django_countries import CountryField


__all__ = ("City", "Person", "Conference")


class CoordField(CompositeField):
    lat = models.FloatField()
    lon = models.FloatField()


class City(models.Model):
    """
    Representation of City model - basic
    place where Conference will be.
    """
    country = CountryField()
    name = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    location = CoordField()

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __unicode__(self):
        return "City: {}".format(self.name_en)


class Person(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)

    email = models.EmailField(max_length=255)
    loc = models.ForeignKey(City)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def __unicode__(self):
        return "Person: {}".format(self.name_en)


class Conference(models.Model):
    title = models.CharField(max_length=128)
    title_en = models.CharField(max_length=128)

    location = models.ForeignKey(City)
    chairman = models.ForeignKey(Person)
    team = models.ManyToManyField(
        Person, null=True, blank=True,
        related_name="conferences+")

    date = models.DateField()

    class Meta:
        verbose_name = _("Conference")
        verbose_name_plural = _("Conferences")

    def __unicode__(self):
        return "Conference: {}".format(self.title_en)
