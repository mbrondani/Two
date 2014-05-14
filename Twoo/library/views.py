# -*- coding: utf-8 -*-

"""

Produz o conteudo das paginas!


Resumindo:

1 - Uma requisi��o chega a /hello/.
2 - Django determina o URLconf raiz analisando a configura��o ROOT_URLCONF.
3 - Django examina todas as URLpatterns no URLconf at� encontrar a primeira que case com /hello/.
4 - Se for casado, � chamado a fun��o view associada.
5 - A fun��o view retorna um HttpResponse.
6 - Django converte o HttpResponse para uma resposta HTTP, que resulta em uma p�gina Web.

"""

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from library.models import *
from library.forms import *

def home(request):
    
    return render(request, 'index.html')


def cadBiblioteca(request):
    
    biblioteca = Biblioteca.objects.all() #Lista de bibliotecas | query
    if request.method == "POST":
        form = FormBiblioteca(request.POST)
        if form.is_valid(): # Processando o Formulario
            nova_lib = form.save()
            HttpResponseRedirect(reverse('nCadLib'))
    else:
        form = FormBiblioteca()
    
    return render(request, 'cadastro_library.html')


def cadLivro(request):
    
    livros = Livro.objects.all() 
    if request.method == "POST":
        form = FormLivro(request.POST)
        if form.is_valid(): 
            novo_livro = form.save()
            HttpResponseRedirect(reverse('nCadLivro'))
    else:
        form = FormLivro()
                        
    return render(request, 'cadastro_livro.html')

    
def cadUsuario(request):
    
    usuarios = Usuario.objects.all() 
    if request.method == "POST":
        form = FormUsuario(request.POST)
        if form.is_valid(): 
            novo_usuario = form.save()
            HttpResponseRedirect(reverse('nCadUsuario'))
    else:
        form = FormUsuario()
                        
    return render(request, 'cadastro_usuario.html')


def cadFuncionario(request):
    
    funcionarios = Funcionario.objects.all()
    if request.method == "POST":
        form = FormFuncionario(request.POST)
        if form.is_valid():
            novo_funcionario = form.save()
            HttpResponseRedirect('nCadFunc')
    else:
        form = FormFuncionario()
    
    return render(request,'cadastro_funcionario.html')


def cadEmprestimo(request):
    
    emprestimos = Emprestimo.objects.all()
    if request.method == "POST":
        form = FormEmprestimo(request.POST)
        if form.is_valid():
            novo_emprestimo = form.save()
            HttpResponseRedirect ('nEmprestimo')
    else:
        form = FormEmprestimo()
        
    return render(request, 'emprestimos.html')


def pesqLivro(request):
    return render(request, 'pesquisa_livro.html')


def pesqUsuario(request):
    return render(request, 'pesquisa_usuario.html')


def pesqFuncionario(request):
    return render(request, 'pesquisa_funcionario.html')


def relatorios(request):
    return render(request, 'relatorios.html')



"""

Cada fun��o view tem pelo menos um parametro chamado request.
� o objeto que cont�m informa��o sobre a requisi��o Web atual que 
ativou a view, e � uma inst�ncia da classe django.http.HttpRequest. 

Nesse exemplo n�o � feito nada com request, mas de qualquer modo deve 
ser o primeiro parametro da view.

"""
