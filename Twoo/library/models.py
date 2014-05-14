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
    telefone = models.CharField(max_length = 12)

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
        return "%s | %s " %(self.titulo, self.autor)
    
    
class Usuario(models.Model):
    
    nome = models.CharField(max_length = 100)
    d_nasc = models.CharField(max_length = 10)
    cpf = models.CharField(max_length = 14)
    telefone = models.CharField(max_length = 12)
    endereco = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 75)
    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=True)
    
    def __unicode(self):
        return self.nome
    
    
class Funcionario(models.Model):
    
    cargo = models.CharField(max_length = 100)
    nome = models.CharField(max_length = 100)
    d_nasc = models.CharField(max_length = 10)
    cpf = models.CharField(max_length = 14)
    endereco = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 75)
    senha = models.EmailField(max_length = 15)
    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=True)
    

class Emprestimo(models.Model):
    pass    

#===============================================================================#
# Criar outros Models
#===============================================================================#