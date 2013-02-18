from django.db import models


__all__ = ("CitiesManager")


class CitiesManager(models.Manager):
    def verified(self):
        return super(CitiesManager, self)\
            .get_query_set()\
            .filter(is_verified=True)
