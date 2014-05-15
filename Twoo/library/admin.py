# -*- coding: utf-8 -*-


## --------------------------- IMPORTS

from django.contrib import admin
from library.models import *


## ------------------------------------------- START REGISTROS


admin.site.register(Biblioteca)
admin.site.register(Livro)


## ------------------------------------------- END REGISTROS