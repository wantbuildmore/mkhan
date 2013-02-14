from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import \
    staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="base.html")),
    # Examples:
    # url(r'^$', 'cityconf.views.home', name='home'),
    # url(r'^cityconf/', include('cityconf.foo.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns()
