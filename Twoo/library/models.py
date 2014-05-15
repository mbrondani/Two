# -*- coding: utf-8 -*-


## --------------------------- IMPORTS

from django.db import models


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
    
    
class Usuario(models.Model):
    
    nome = models.CharField(max_length = 100)
    d_nasc = models.CharField(max_length = 10)
    cpf = models.CharField(max_length = 14)
    telefone = models.CharField(max_length = 12)
    endereco = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 75)
    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)
    
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
    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)
    

class Emprestimo(models.Model):
    
    cod_livro = models.IntegerField(max_length = 10)
    titulo = titulo = models.CharField(max_length = 150)
    cod_usuario = models.IntegerField(max_length = 10)
    cod_func = models.IntegerField(max_length = 10)
    endereco = endereco = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 75)
    pedido = models.DateField()
    devolucao = models.DateField()
    biblioteca = models.ForeignKey(Biblioteca, blank=True, null=False)


## ------------------------------------------- START MODELS


#===============================================================================
#                             Observações
# querySet = Lista de Objetos
# Field = Classe responsavel por validação
# Widget = Representação do Field em HTML
#
#===============================================================================
