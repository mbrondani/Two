# -*- coding: utf-8 -*-

"""

As URLs para este projeto Django. Pense nisso como como uma 
"tabela de conteudo" para o seu site em Django.

Mapeamento entre URL's e funções View que devem ser chamadas 
por essas URL's.

"""

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static 
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from library.views import cadLivro, cadUsuario, cadFuncionario, emprestimo, teste

# Definiçao do mapeamento entre urls e o codigo que as manipula.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Twoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    
    #===============================================================================#
    #                                URL's Library                                  #
    
    url(r'^$', 'library.views.home', name='nHome'),
    url(r'^cadLivro/$', cadLivro, name='nCadLivro'),
    url(r'^cadUsuario/$', cadUsuario, name='nCadUsuario'),
    url(r'^cadFuncionario/$', cadFuncionario, name='nCadFuncionario'),
    url(r'^emprestimo$', emprestimo, name='nEmprestimo'),
    
    #===============================================================================#
    
    url(r'^testetemplate/$', teste, name='nTeste'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
