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


## ------------------------------------------- START VIEWS


def index(request):

    next = request.REQUEST.get('next', 'cadBiblioteca')

    username = request.REQUEST.get('username')
    password = request.REQUEST.get('password')

    bibliotecas = Biblioteca.objects.all()
    user = authenticate(username=username, password=password)

    if user is not None and user.is_active:
        login(request, user)
        if len(bibliotecas)<1:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(reverse('nHome'))

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

    biblioteca = Biblioteca.objects.all()
    form = FormBiblioteca(request.POST)
    if request.method == "POST" and form.is_valid():
        nova_lib = form.save()
        return HttpResponseRedirect(reverse('nHome'))
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
    form = FormLivro(request.POST)
    if request.method == "POST" and form.is_valid():
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
def cadPessoa(request):

    usuarios = Pessoa.objects.all()
    form = FormPessoa(request.POST)
    if request.method == "POST" and form.is_valid():
        novo_usuario = form.save()
        return HttpResponseRedirect(reverse('nCadUsuario'))
    else:
        form = FormPessoa()

    return render(request, 'cadastro_usuario.html',
                {
                    'form':form,
                }
            )


@login_required
def cadEmprestimo(request):

    emprestimos = Emprestimo.objects.all()
    form = FormEmprestimo(request.POST)
    if request.method == "POST" and form.is_valid():
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

    pesquisa = request.REQUEST.get('pesquisa')
    oLivro = Livro.objects.filter(codigo = pesquisa)

    return render(request, 'pesquisa_livro.html',
                {
                    'oLivro': oLivro,
                }
            )


@login_required
def pesqUsuario(request):

    pesquisa = request.REQUEST.get('pesquisa')
    oPessoa = Pessoa.objects.filter(pk = pesquisa)

    return render(request, 'pesquisa_usuario.html',
                {
                    'oPessoa': oPessoa,
                }
            )


## --------------------------- END PESQUISAS


## --------------------------- START DELETE

@login_required
def delLivro(request):

    codigo = request.REQUEST.get('codigo')
    oLivro = Livro.objects.get(pk = codigo)

    if request.method == "POST" and oLivro is not None:
        oLivro.delete()
        return HttpResponseRedirect('')

    return render(request, 'template.html')


@login_required
def delPessoa(request):

    codigo = request.REQUEST.get('codigo')
    oPessoa = Pessoa.objects.get(pk = codigo)

    if request.method == "POST" and oPessoa is not None:
        oPessoa.delete()
        return HttpResponseRedirect('')

    return render(request, 'template.html')


## --------------------------- END DELETE


## --------------------------- START UPDATES

def upLivro(request):

    codigo = request.REQUEST.get('codigo')
    oLivro = Livro.objects.get(pk=codigo)

    if request.method == 'POST':
        form = FormLivro(request.POST, instance=oLivro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = FormLivro(instance=oLivro)

    return render(request,'template.html',
                {
                    'form':form,
                    'codigo':codigo,
                }
            )

def upPessoa(request):

    codigo = request.REQUEST.get('codigo')
    oPessoa = Pessoa.objects.get(pk=codigo)

    if request.method == 'POST':
        form = FormPessoa(request.POST, instance=oPessoa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = FormPessoa(instance=oPessoa)

    return render(request,'template.html',
                {
                    'form':form,
                    'codigo':codigo,
                }
            )


## --------------------------- END UPDATES


## --------------------------- START FUNCIONALIDADES


@login_required
def statusEmprestimo(request):
    pass


@login_required
def relatorios(request):
    return render(request, 'relatorios.html')


@login_required
def sairSistema(request):
    logout(request)
    return HttpResponseRedirect(reverse('nIndex'))


def acessoNegado(request):
    return render_to_response('acesso_negado.html')


## --------------------------- END FUNCIONALIDADES

## ------------------------------------------- END VIEWS


#===============================================================================
#Produz o conteudo das paginas!
#
#Resumindo:
#
#1 - Uma requisião chega a /hello/.
#2 - Django determina o URLconf raiz analisando a configura��o ROOT_URLCONF.
#3 - Django examina todas as URLpatterns no URLconf at� encontrar a primeira que case com /hello/.
#4 - Se for casado, � chamado a fun��o view associada.
#5 - A fun��o view retorna um HttpResponse.
#6 - Django converte o HttpResponse para uma resposta HTTP, que resulta em uma p�gina Web.
#
# Controllers são chamados de views no Django
#
#Cada funcao view tem pelo menos um parametro chamado request.
#E o objeto que contem informacao sobre a requisicao Web atual que
#ativou a view, e � uma instancia da classe django.http.HttpRequest.
#
#Nesse exemplo n�o � feito nada com request, mas de qualquer modo deve
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
