from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

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
    name = models.CharField(_("City Name"), max_length=128)
    name_en = models.CharField(_("City Name in English"), max_length=128)
    location = CoordField()
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __unicode__(self):
        return "City: {}".format(self.name_en)


class Person(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(_("Name"), max_length=128)
    name_en = models.CharField(_("Name in english"), max_length=128)

    email = models.EmailField(_("Email"), max_length=255)
    loc = models.ForeignKey(City)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def get_absolut_url(self):
        # TODO: use `url_for` for such kind of methods
        # return reverse('author-detail', kwargs={'pk': self.pk})
        return ''

    def __unicode__(self):
        return "Person: {}".format(self.name_en)


class Conference(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    title_en = models.CharField(_("Title in english"), max_length=128)

    location = models.ForeignKey(City)
    chairman = models.ForeignKey(Person)
    team = models.ManyToManyField(
        Person, null=True, blank=True,
        related_name="conferences+")

    date = models.DateField(_("When"))
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Conference")
        verbose_name_plural = _("Conferences")

    def __unicode__(self):
        return "Conference: {}".format(self.title_en)
