# -*- coding: utf-8 -*-


## --------------------------- IMPORTS

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, date

## ------------------------------------------- START MODELS


class Biblioteca(models.Model):

    endereco = models.CharField(max_length = 80)
    nome = models.CharField(max_length = 60)
    telefone = models.CharField(max_length = 12)

    def __unicode__(self):
        return self.nome


class Livro(models.Model):

    codigo = models.CharField('Codigo', max_length = 10)
    publicacao = models.CharField('Ano de Publicação', max_length = 10)
    autor = models.CharField('Autor', max_length = 80)
    editora = models.CharField('Editora', max_length = 45)
    genero = models.CharField('Genero', max_length = 45)
    titulo = models.CharField('Titulo', max_length = 150)

    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)

    def __unicode__(self):
        return "%s | %s " %(self.titulo, self.autor)


class Pessoa(models.Model):

    codigo = models.CharField('Codigo', max_length = 10)
    nome = models.CharField('Nome', max_length = 100)
    d_nasc = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF',max_length = 14)
    telefone = models.CharField('Telefone',max_length = 12)
    endereco = models.CharField('Endereço',max_length = 200)
    email = models.EmailField('E-mail',max_length = 75)
    tipo = models.CharField('Tipo',max_length = 100)

    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)

    def __unicode__(self):
        return self.nome


class Emprestimo(models.Model):

    cod_livro = models.CharField('Codigo do Livro (ID)', max_length = 10)
    titulo = models.CharField('Titulo', max_length = 150)
    cod_usuario = models.CharField('Codigo do Responsavel', max_length = 10)
    cod_func = models.CharField('Codigo do Funcionario', max_length = 10)
    endereco = models.CharField('Endereço Responsavel', max_length = 200)
    email = models.EmailField('E-mail Responsavel', max_length = 75)
    pedido = models.DateField('Data do Pedido', default=datetime.now, blank=True)
    devolucao = models.DateField('Data da Devolução', blank=True)

    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)

    def __unicode__(self):
        return "%s | %s" %(self.pk, self.cod_livro)


class UserSystem (models.Model):

    user = models.OneToOneField(
        User,
        related_name = 'user_system'
    )

    def __unicode__(self):
        return self.user.username



## ------------------------------------------- START MODELS


##def dataEntrega():
##    days = 20
##    dateNow = date.today()
##    return date.fromordinal(dateNow.toordinal() + days)
##
##dataEntrega = dataEntrega()


#===============================================================================
#                             Observacoes
# querySet = Lista de Objetos
# Field = Classe responsavel por validacao
# Widget = Representacao do Field em HTML
#
#===============================================================================
