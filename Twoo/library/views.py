# -*- coding: utf-8 -*-


## --------------------------- IMPORTS

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required


from library.models import *
from library.forms import *
from Twoo import settings


## ------------------------------------------- START VIEWS


def index(request):
    
    next = request.REQUEST.get('next', 'cadBiblioteca')
    username = request.REQUEST.get('username')
    password = request.REQUEST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(next)

    return render(request, 'index.html',
                {
                    'next':next,
                }
            )


def cadSistema(request):
    
    novo_usuario = User.objects.all()
    if request.method == "POST":
        
        username = request.REQUEST.get('username') 
        email = request.REQUEST.get('email') 
        password = request.REQUEST.get('password')
        
        novo_usuario = User.objects.create_user(username, email, password)
        novo_usuario.save()
        return HttpResponseRedirect(reverse('nIndex'))        
    else:
        pass
        
    return render(request, 'cadastro_sistema.html')


@login_required
def home(request):
    return render(request, 'home.html')


## --------------------------- START CADASTROS

@login_required
def cadBiblioteca(request):
    
    biblioteca = Biblioteca.objects.all() #Lista de bibliotecas | query
    if request.method == "POST":
        form = FormBiblioteca(request.POST)
        if form.is_valid(): # Processando o Formulario
            nova_lib = form.save()
            return HttpResponseRedirect(reverse('nCadLib'))
    else:
        form = FormBiblioteca()
    
    return render(request, 'cadastro_library.html',
                {
                    'form':form,                                 
                }
            )


@login_required
def cadLivro(request):
    
    livros = Livro.objects.all() 
    if request.method == "POST":
        form = FormLivro(request.POST)
        if form.is_valid(): 
            novo_livro = form.save()
            return HttpResponseRedirect(reverse('nCadLivro'))
    else:
        form = FormLivro()
                        
    return render(request, 'cadastro_livro.html',
                {
                    'form':form,                                 
                }
            )


@login_required
def cadUsuario(request):
    
    usuarios = Usuario.objects.all() 
    if request.method == "POST":
        form = FormUsuario(request.POST)
        if form.is_valid(): 
            novo_usuario = form.save()
            return HttpResponseRedirect(reverse('nCadUsuario'))
    else:
        form = FormUsuario()
                        
    return render(request, 'cadastro_usuario.html',
                {
                    'form':form,                                 
                }
            )


@login_required
def cadFuncionario(request):
    
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        form = FormFuncionario(request.POST)
        if form.is_valid():
            novo_funcionario = form.save()
            return HttpResponseRedirect(reverse('nCadFunc'))
    else:
        form = FormFuncionario()
    
    return render(request,'cadastro_funcionario.html',
                {
                    'form':form,                                 
                }
            )

@login_required
def cadEmprestimo(request):
    
    emprestimos = Emprestimo.objects.all()
    if request.method == "POST":
        form = FormEmprestimo(request.POST)
        if form.is_valid():
            novo_emprestimo = form.save()
            return HttpResponseRedirect(reverse('nEmprestimo'))
    else:
        form = FormEmprestimo()
        
    return render(request, 'emprestimos.html',
                {
                    'form':form,                                 
                }
            )


## --------------------------- END CADASTROS

## --------------------------- START PESQUISAS

@login_required
def pesqLivro(request):
    return render(request, 'pesquisa_livro.html')

@login_required
def pesqUsuario(request):
    return render(request, 'pesquisa_usuario.html')

@login_required
def pesqFuncionario(request):
    return render(request, 'pesquisa_funcionario.html')


## --------------------------- END CADASTROS

## --------------------------- START FUNCIONALIDADES

@login_required
def relatorios(request):
    return render(request, 'relatorios.html')

@login_required
def sairSistema(request):
    logout(request)
    return HttpResponseRedirect(reverse('nIndex'))

def acessoNegado(request):
    return render_to_response('acesso_negado.html')


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
