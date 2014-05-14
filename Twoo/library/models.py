# -*- coding: utf-8 -*-

from django.db import models
from time import strftime

#===============================================================================
#                             Observações
# querySet = Lista de Objetos
# Field = Classe responsavel por validação
# Widget = Representação do Field em HTML
#
#===============================================================================


class Biblioteca(models.Model):

    endereco = models.CharField(max_length = 80)
    nome = models.CharField(max_length = 60)
    telefone = models.IntegerField(max_length = 11)

    def __unicode__(self):
        return self.nome

class Livro(models.Model):
    codigo = models.CharField(max_length = 10)
    publicacao = models.IntegerField()
    autor = models.CharField(max_length = 80)
    editora = models.CharField(max_length = 45)
    genero = models.CharField(max_length = 45)
    sinopse = models.CharField(max_length=150)
    titulo = models.CharField(max_length = 150)
    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=True)
    
    def __unicode__(self):
        return (self.titulo)

#===============================================================================#
# Criar outros Models
#===============================================================================#