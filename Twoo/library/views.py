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

Cada fun��o view tem pelo menos um parametro chamado request.
� o objeto que cont�m informa��o sobre a requisi��o Web atual que 
ativou a view, e � uma inst�ncia da classe django.http.HttpRequest. 

Nesse exemplo n�o � feito nada com request, mas de qualquer modo deve 
ser o primeiro parametro da view.

"""
