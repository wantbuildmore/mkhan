from django_assets import Bundle, register

core_css = Bundle(
    'core/foundation/stylesheets/foundation.css',
    'core/css/base.css',
    filters='cssmin',
    output='core.css')

register('core_css', core_css)
