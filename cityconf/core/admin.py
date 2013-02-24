from django.contrib import admin

from core.models import City, Person, Conference


class CityAdmin(admin.ModelAdmin):
    list_filter = ('is_verified',)


class ConferenceAdmin(admin.ModelAdmin):
    list_filter = ('is_verified', 'is_visible')


admin.site.register(City, CityAdmin)
admin.site.register(Person)
admin.site.register(Conference, ConferenceAdmin)
