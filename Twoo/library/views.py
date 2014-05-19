# -*- coding: utf-8 -*-


## --------------------------- IMPORTS

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from library.models import *
from library.forms import *


## ------------------------------------------- START VIEWS


def index(request):
    
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


## --------------------------- START CADASTROS


def cadBiblioteca(request):
    
    biblioteca = Biblioteca.objects.all() #Lista de bibliotecas | query
    if request.method == "POST":
        form = FormBiblioteca(request.POST)
        if form.is_valid(): # Processando o Formulario
            nova_lib = form.save()
            HttpResponseRedirect(reverse('nCadLib'))
    else:
        form = FormBiblioteca()
    
    return render(request, 'cadastro_library.html',
                {
                    'form':form,                                 
                }
            )



def cadLivro(request):
    
    livros = Livro.objects.all() 
    if request.method == "POST":
        form = FormLivro(request.POST)
        if form.is_valid(): 
            novo_livro = form.save()
            HttpResponseRedirect(reverse('nCadLivro'))
    else:
        form = FormLivro()
                        
    return render(request, 'cadastro_livro.html',
                {
                    'form':form,                                 
                }
            )


    
def cadUsuario(request):
    
    usuarios = Usuario.objects.all() 
    if request.method == "POST":
        form = FormUsuario(request.POST)
        if form.is_valid(): 
            novo_usuario = form.save()
            HttpResponseRedirect(reverse('nCadUsuario'))
    else:
        form = FormUsuario()
                        
    return render(request, 'cadastro_usuario.html',
                {
                    'form':form,                                 
                }
            )



def cadFuncionario(request):
    
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        form = FormFuncionario(request.POST)
        if form.is_valid():
            novo_funcionario = form.save()
            HttpResponseRedirect(reverse('nCadFunc'))
    else:
        form = FormFuncionario()
    
    return render(request,'cadastro_funcionario.html',
                {
                    'form':form,                                 
                }
            )


def cadEmprestimo(request):
    
    emprestimos = Emprestimo.objects.all()
    if request.method == "POST":
        form = FormEmprestimo(request.POST)
        if form.is_valid():
            novo_emprestimo = form.save()
            HttpResponseRedirect(reverse('nEmprestimo'))
    else:
        form = FormEmprestimo()
        
    return render(request, 'emprestimos.html',
                {
                    'form':form,                                 
                }
            )


## --------------------------- END CADASTROS

## --------------------------- START PESQUISAS


def pesqLivro(request):
    return render(request, 'pesquisa_livro.html')


def pesqUsuario(request):
    return render(request, 'pesquisa_usuario.html')


def pesqFuncionario(request):
    return render(request, 'pesquisa_funcionario.html')


## --------------------------- END CADASTROS

## --------------------------- START FUNCIONALIDADES


def relatorios(request):
    return render(request, 'relatorios.html')


def cadSistema(request):
    
    usuario = User.objects.all()
    if request.method == "POST":
        
        username = request.REQUEST.get('username') 
        email = request.REQUEST.get('email') 
        password = request.REQUEST.get('password')
        
        usuario = User.objects.create_user(username, email, password)
        usuario.save()
        return HttpResponseRedirect(reverse('nIndex'))        
    else:
        return HttpResponseRedirect(reverse('nCadSistema'))
        
    return render(request, 'cadastro_sistema.html',
                {
                    
                }
            )


## --------------------------- START FUNCIONALIDADES

## ------------------------------------------- END VIEWS


#===============================================================================
#Produz o conteudo das paginas!
#
#Resumindo:
#
#1 - Uma requisição chega a /hello/.
#2 - Django determina o URLconf raiz analisando a configuração ROOT_URLCONF.
#3 - Django examina todas as URLpatterns no URLconf até encontrar a primeira que case com /hello/.
#4 - Se for casado, é chamado a função view associada.
#5 - A função view retorna um HttpResponse.
#6 - Django converte o HttpResponse para uma resposta HTTP, que resulta em uma página Web.
#
#
#Cada função view tem pelo menos um parametro chamado request.
#É o objeto que contém informação sobre a requisição Web atual que 
#ativou a view, e é uma instância da classe django.http.HttpRequest. 
#
#Nesse exemplo não é feito nada com request, mas de qualquer modo deve 
#ser o primeiro parametro da view.
#===============================================================================

#===============================================================================
#
# from django.contrib.auth.models import User
# usuario = User.objects.create_user(username, email, password)
# usuario.first_name = 'Rayane'
# usuario.last_name = 'Paiva'
# usuario.save()
# usuario.is_superuser = True
# usuario.set_password('novasenha')
# usuario.save()
#
#===============================================================================
#
# usuario = User.objects.get(id=1)
# profile = UserSystem.objects.create(user = usuario)
# 
#===============================================================================
