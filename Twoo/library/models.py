# -*- coding: utf-8 -*-

from django.db import models
from time import strftime

# Create your models here.
# Criação dos models


class Biblioteca(models.Model):

    endereco = models.CharField('Endereço', max_length = 80)
    nome = models.CharField('Nome', max_length = 60)
    telefone = models.IntegerField('Telefone', max_length = 11)

    def __unicode__(self):
        return self.nome

class Livro(models.Model):

    ano_publicacao = models.CharField('Ano de Publicação', max_length = 4)
    autor = models.CharField('Autor',max_length = 80)
    editora = models.CharField(max_length = 45)
    genero = models.CharField(max_length = 45)
    sinopse = models.TextField('Resumo do Livro')
    titulo = models.CharField('Titulo',max_length = 150)
    biblioteca = models.ForeignKey(Biblioteca)

    def __unicode__(self):
        return self.titulo