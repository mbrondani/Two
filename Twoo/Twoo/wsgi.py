# -*- coding: utf-8 -*-

"""
WSGI config for Twoo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/

# ------------------------------------------------------ #

Um ponto de entrada para o WSGI compatíveis com servidores 
web para servir o seu projeto. Veja como fazer deploy com 
WSGI (https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/) 
para maiores detalhes.

"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Twoo.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
