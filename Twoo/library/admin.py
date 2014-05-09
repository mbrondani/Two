# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
# Registro dos Models

# realiza import relativo
from . models import Biblioteca, Livro


admin.site.register(Biblioteca)
admin.site.register(Livro)
