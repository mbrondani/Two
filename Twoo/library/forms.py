# -*- coding: utf-8 -*-

#===============================================================================
# Formularios Django
#===============================================================================

from django import forms


class FormLivro(forms.Form):
    
    publicacao = forms.CharField(max_length=4)
    autor = forms.CharField(max_length=80)
    editora = forms.CharField(max_length=45)
    genero = forms.CharField(max_length=45)
    sinopse = forms.Textarea()
    titulo = forms.CharField(max_length=150)
    