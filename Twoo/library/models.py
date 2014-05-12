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
    biblioteca = models.OneToOneField(Biblioteca)

    def __unicode__(self):
        return (self.titulo, self.autor)

#===============================================================================#
# Criar outros Models
#===============================================================================#

'''

class Usuario(models.Model):
    pass

class Funcionario(models.Model):
    pass

class Emprestimo(models.Model):
    
    codLivro = models.OneToOneField(Livro)
    titulo = models.CharField(max_length = 80)
    usuario = models.OneToOneField(Usuario)
    funcionario = models.OneToOneField(Funcionario)
    endereco = models.CharField(max_length = 80)
    email = models.EmailField()
    dt_saida = models.DateField()
    dt_devolucao = models.DateField()

'''