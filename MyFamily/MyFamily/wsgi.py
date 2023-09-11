"""
WSGI config for MyFamily project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/pavani/MyFamily/MyFamily/'

if path not in sys.path:

    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFamily.settings')

application = get_wsgi_application()




