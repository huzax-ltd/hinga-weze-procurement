"""
WSGI config for hinga-weze-procurement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from app import settings

if settings.IS_LOCAL:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hinga-weze-procurement.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hinga_weze_procurement.settings")

application = get_wsgi_application()
