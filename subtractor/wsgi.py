"""
WSGI config for subtractor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subtractor.settings")


application = Cling(get_wsgi_application())



# original code, deferring to heroku code above for now...
# application = get_wsgi_application()

# application = get_wsgi_application()   # ORIGINAL DJANGO CODE. REPLACED BY BELOW FOR SERVING STATIC FILES


