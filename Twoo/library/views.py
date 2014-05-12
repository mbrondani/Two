# -*- coding: utf-8 -*-

"""

Produz o conteudo das paginas!


Resumindo:

1 - Uma requisição chega a /hello/.
2 - Django determina o URLconf raiz analisando a configuração ROOT_URLCONF.
3 - Django examina todas as URLpatterns no URLconf até encontrar a primeira que case com /hello/.
4 - Se for casado, é chamado a função view associada.
5 - A função view retorna um HttpResponse.
6 - Django converte o HttpResponse para uma resposta HTTP, que resulta em uma página Web.

"""

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect

from library.models import Livro
from django.core.urlresolvers import reverse

# Create your views here.

def home(request):

    return render(request, 'index.html')

    # return render_to_response('index.html') 
    # render(request, template, contexto)

def cadLivro(request):
    
    livros = Livro.objects.all() # Lista de livros

    if request.method == "POST":
        
        codigo = request.POST.get('codigo')
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        genero = request.POST.get('genero')
        publicacao = request.POST.get('publicacao')
        sinopse = request.POST.get('sinopse')
        
        novo_livro = Livro(
                        'codigo': codigo,
                        'titulo': titulo,
                        'autor': autor,
                        'editora': editora,
                        'genero': genero,
                        'publicacao': publicacao,
                        'sinopse': sinopse,
                    )
        novo_livro.save()
        HttpResponseRedirect(reverse('nCadLivro'))
                
    return render(request, 'cadastro_livro.html', 
                  {
                    'livros': livros,
                  }
                )
    
    # Sem formularios
    # nao eh necessario referenciar a pasta templates
    # render_to_response(template)
    
def cadUsuario(request):
    return render_to_response('cadastro_usuario.html')

def cadFuncionario(request):
    return render_to_response('cadastro_funcionario.html')

def emprestimo(request):
    return render_to_response('emprestimos.html')

def teste(request):
    return render_to_response('library.html')


"""

Cada função view tem pelo menos um parametro chamado request.
É o objeto que contém informação sobre a requisição Web atual que 
ativou a view, e é uma instância da classe django.http.HttpRequest. 

Nesse exemplo não é feito nada com request, mas de qualquer modo deve 
ser o primeiro parametro da view.

"""
