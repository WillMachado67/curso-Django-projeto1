from .instaled_apps import INSTALLED_APPS
from .middleware import MIDDLEWARE

INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    ] + MIDDLEWARE

# Django debug tool bar
INTERNAL_IPS = [
    '127.0.0.1',
]