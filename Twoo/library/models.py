# -*- coding: utf-8 -*-


## --------------------------- IMPORTS

from django.db import models
from django.contrib.auth.models import User


## ------------------------------------------- START MODELS


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

    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)

    def __unicode__(self):
        return "%s | %s " %(self.titulo, self.autor)


class Pessoa(models.Model):

    codigo = models.CharField('Codigo', max_length = 10)
    nome = models.CharField('Nome', max_length = 100)
    d_nasc = models.CharField('Data de Nascimento', max_length = 10)
    cpf = models.CharField('CPF',max_length = 14)
    telefone = models.CharField('Telefone',max_length = 12)
    endereco = models.CharField('Endereço',max_length = 200)
    email = models.EmailField('E-mail',max_length = 75)
    tipo = models.CharField('Tipo',max_length = 100)

    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)

    def __unicode(self):
        return self.nome


class Emprestimo(models.Model):

    cod_livro = models.CharField('Codigo do Livro (ID)', max_length = 10)
    titulo = titulo = models.CharField('Titulo', max_length = 150)
    cod_usuario = models.CharField('Codigo do Responsavel', max_length = 10)
    cod_func = models.CharField('Codigo do Funcionario', max_length = 10)
    endereco = endereco = models.CharField('Endereço Responsavel', max_length = 200)
    email = models.EmailField('E-mail Responsavel', max_length = 75)
    pedido = models.DateField('Data do Pedido', )
    devolucao = models.DateField('Data da Devolução', )

    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)


class UserSystem (models.Model):

    user = models.OneToOneField(
        User,
        related_name = 'user_system'
    )

    def __unicode__(self):
        return self.user.username



## ------------------------------------------- START MODELS


#===============================================================================
#                             Observa��es
# querySet = Lista de Objetos
# Field = Classe responsavel por valida��o
# Widget = Representa��o do Field em HTML
#
#===============================================================================
