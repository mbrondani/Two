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

    url(r'^cadSistema/$', 'library.views.cadSistema', name='nCadSistema'),
    url(r'^cadBiblioteca/$', 'library.views.cadBiblioteca', name='nCadLib'),

    url(r'^cadLivro/$', 'library.views.cadLivro', name='nCadLivro'),
    url(r'^cadPessoa/$', 'library.views.cadPessoa', name='nCadUsuario'),

    url(r'^emprestimo$', 'library.views.cadEmprestimo', name='nEmprestimo'),

    url(r'^pesqLivro/$', 'library.views.pesqLivro', name='nPesqLivro'),
    url(r'^pesqUsuario/$', 'library.views.pesqUsuario', name='nPesqUsuario'),

    url(r'^relatorios/$', 'library.views.relatorios', name='nRelatorios'),

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
#Mapeamento entre URL's e fun��es View que devem ser chamadas
#por essas URL's.
#
#urlpatterns: Defini�ao do mapeamento entre urls e o codigo que as manipula.
#
# Examples:
# url(r'^$', 'Twoo.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
# url(r'^admin/', include(admin.site.urls)),
#
#
#===============================================================================#
