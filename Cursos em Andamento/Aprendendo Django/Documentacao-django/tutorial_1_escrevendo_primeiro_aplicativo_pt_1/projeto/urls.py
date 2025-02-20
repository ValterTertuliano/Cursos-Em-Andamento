"""
Configuração de URLs para o projeto 'projeto'.

A lista `urlpatterns` mapeia URLs para views. Para mais informações, consulte:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Exemplos:3

Views baseadas em função:
    1. Adicione uma importação:  from my_app import views
    2. Adicione uma URL à lista de urlpatterns:  path('', views.home, name='home')

Views baseadas em classe:
    1. Adicione uma importação:  from other_app.views import Home
    2. Adicione uma URL à lista de urlpatterns:  path('', Home.as_view(), name='home')

Incluindo outra configuração de URLs:
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL à lista de urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importação do módulo 'admin' do Django
# O 'admin' é o módulo que permite a criação de uma interface administrativa
# para gerenciar o conteúdo do site. O caminho 'admin.site.urls' é o que permite
# que a interface de administração esteja acessível.
from django.contrib import admin  # type: ignore

# Importação das funções 'path' e 'include' de 'django.urls'
# O 'path' é utilizado para definir rotas de URL para views, enquanto o 'include'
# é usado para incluir outros arquivos de configuração de URLs (por exemplo,
# as URLs de um aplicativo específico).
from django.urls import path, include  # type: ignore

# A lista 'urlpatterns' é onde todas as URLs do projeto são mapeadas para as views.
# Essa lista será usada pelo Django para verificar se a URL solicitada pelo usuário
# corresponde a alguma das rotas definidas aqui e, em caso afirmativo, chamar a
# view correspondente.

urlpatterns = [
    # A primeira rota mapeia a URL raiz ('') para o arquivo 'urls.py' do aplicativo 'inicio'.
    # Isso significa que qualquer acesso à raiz do site será direcionado para as URLs
    # definidas dentro do aplicativo 'inicio'.
    path("", include("inicio.urls")),
    # A segunda rota mapeia a URL 'admin/' para a interface administrativa do Django.
    # Isso permitirá acessar o painel de administração do Django em 'www.seusite.com/admin/'.
    path("admin/", admin.site.urls),
]

# Resumo:
# - A URL raiz ('') irá redirecionar para o arquivo de URLs do aplicativo 'inicio'.
# - A URL 'admin/' redireciona para a interface administrativa padrão do Django.
# Dessa forma, o Django irá procurar as URLs específicas dentro do aplicativo 'inicio'
# para rotas adicionais, como a página inicial, por exemplo.
