from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import \
    staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="core/base.html")),
    url(r'', include('social_auth.urls')),
    url(r'', include('core.urls')),
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += staticfiles_urlpatterns()
