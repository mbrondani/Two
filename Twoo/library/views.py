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
from django.http.response import HttpResponse

# Create your views here.



def cadLivro(request):
    # nao eh necessario referenciar a pasta templates
    return render_to_response('cadastro_livro.html') # render_to_response(template)

def home(request):
    
    return render(request, 'index.html', {'email':''}) # render(request, template, contexto)

def homeY (request):
    return HttpResponse("INDEX");


"""

Cada função view tem pelo menos um parametro chamado request.
É o objeto que contém informação sobre a requisição Web atual que 
ativou a view, e é uma instância da classe django.http.HttpRequest. 

Nesse exemplo não é feito nada com request, mas de qualquer modo deve 
ser o primeiro parametro da view.

"""
