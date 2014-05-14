# -*- coding: utf-8 -*-

#===============================================================================
# Formularios Django
#===============================================================================

from django import forms
from library.models import Livro


class FormLivro(forms.Form):
    
    codigo = forms.CharField(max_length=10)
    publicacao = forms.IntegerField()
    autor = forms.CharField(max_length=80)
    editora = forms.CharField(max_length=45)
    genero = forms.CharField(max_length=45)
    sinopse = forms.CharField(max_length=150)
    titulo = forms.CharField(max_length=150)
    
    def save(self):
        
        codigo = self.cleaned_data.get('codigo')# Acessando os Fields
        publicacao = self.cleaned_data.get('publicacao')         
        autor = self.cleaned_data.get('autor')
        editora = self.cleaned_data.get('editora')
        genero = self.cleaned_data.get('genero')
        sinopse = self.cleaned_data.get('sinopse')
        titulo = self.cleaned_data.get('titulo')
        
        novo_livro = Livro(
            codigo = codigo,
            publicacao = publicacao,
            autor = autor,
            editora = editora,
            genero = genero,
            sinopse = sinopse,
            titulo = titulo
        )
        novo_livro.save()
        return novo_livro 
    
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if Livro.objects.filter(codigo = codigo ):
            raise forms.ValidationError('Codigo já cadastrado!')
        return codigo