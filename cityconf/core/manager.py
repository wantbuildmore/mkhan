from django.db import models


__all__ = ("CitiesManager", "ConferencesManager")


class CitiesManager(models.Manager):
    def suggested_by(self, user, verified=None):
        """
        Return list of cities suggested by
        ``user``, also able to
        get verified or not verified.

        By default return both verified and
        not verified cities by provided user.

        Usage::

            # get all cities by particular user
            City.objects.suggested_by(request.user)

            # get verified cities
            City.objects.suggested_by(
                request.user, verified=True)

        """
        qs = super(CitiesManager, self)\
            .get_query_set()\
            .filter(suggested_by=user)

        if verified is not None:
            qs = qs.filter(is_verified=verified)

        return qs

    def verified(self):
        """
        Return only verified cities
        """
        return super(CitiesManager, self)\
            .get_query_set()\
            .filter(is_verified=True)


class ConferencesManager(models.Manager):
    def owned_by(self, user, verified=None):
        """
        Return conferenced by ``user``
        """
        qs = super(ConferencesManager, self)\
            .get_query_set()\
            .filter(owner=user)

        if verified is not None:
            qs = qs.filter(is_verified=verified)

        return qs

    def verified(self):
        """
        Return only verified conferences
        """
        return super(ConferencesManager, self)\
            .get_query_set()\
            .filter(is_verified=True)

    def active(self):
        return self.verified().filter(is_visible=True)
