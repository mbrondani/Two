# -*- coding: utf-8 -*-


## --------------------------- IMPORTS

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

## ------------------------------------------- START URLS


urlpatterns = patterns('',

    #===============================================================================#
    #                                URL's Library                                  #

    url(r'^$', 'library.views.index', name='nIndex'),
    url(r'^home/$', 'library.views.home', name='nHome'),

    url(r'^cadastro/sistema/$', 'library.views.cadSistema', name='nCadSistema'),
    url(r'^cadastro/biblioteca/$', 'library.views.cadBiblioteca', name='nCadLib'),
    url(r'^cadastro/livro/$', 'library.views.cadLivro', name='nCadLivro'),
    url(r'^cadastro/pessoa/$', 'library.views.cadPessoa', name='nCadUsuario'),
    url(r'^cadastro/emprestimo/$', 'library.views.cadEmprestimo', name='nEmprestimo'),

    url(r'^pesquisa/livro/$', 'library.views.pesqLivro', name='nPesqLivro'),
    url(r'^pesquisa/usuario/$', 'library.views.pesqUsuario', name='nPesqUsuario'),
    url(r'^pesquisa/emprestimo/$', 'library.views.pesqEmprestimo', name='nPesqEmpres'),

    url(r'^editar/livro/(?P<id>\d+)/$', 'library.views.upLivro', name='nUpLivro'),
    url(r'^editar/usuario/(?P<id>\d+)/$', 'library.views.upPessoa', name='nUpPessoa'),
    url(r'^editar/emprestimo/(?P<id>\d+)/$', 'library.views.upEmprestimo', name='nUpEmpres'),

    url(r'^deletar/livro/(?P<id>\d+)/$', 'library.views.delLivro', name='nDelLivro'),
    url(r'^deletar/usuario/(?P<id>\d+)/$', 'library.views.delPessoa',name='nDelPessoa'),

    url(r'^relatorios/$', 'library.views.relatorios', name='nRelatorios'),
    url(r'^sobre/$', 'library.views.sobre', name='nSobre'),
    url(r'^ajuda/$', 'library.views.ajuda', name='nContato'),
    url(r'^logout/$', 'library.views.sairSistema', name='nLogout'),

    url(r'^acessoNegado/', 'library.views.acessoNegado', name='nAcessoNeg'),

    #===============================================================================#
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


## ------------------------------------------- END URLS


#===============================================================================#
#
#As URLs para este projeto Django. Pense nisso como como uma
#"tabela de conteudo" para o seu site em Django.
#
#Mapeamento entre URL's e funcoes View que devem ser chamadas
#por essas URL's.
#
#urlpatterns: Definicao do mapeamento entre urls e o codigo que as manipula.
#
# Examples:
# url(r'^$', 'Twoo.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
# url(r'^admin/', include(admin.site.urls)),
#
#
#===============================================================================#
