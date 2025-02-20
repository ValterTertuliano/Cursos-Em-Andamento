# Importação do módulo 'path' de 'django.urls'
# O 'path' é utilizado para definir a URL que será associada a uma view no Django.
# Ele recebe três parâmetros principais:
# 1. O padrão de URL (em formato de string);
# 2. A view que será executada quando essa URL for acessada;
# 3. O nome da URL, que pode ser usado para referenciar a URL em templates ou no código.
from django.urls import path  # type: ignore

# Importação da variável 'views' do módulo 'inicio'
# A variável 'views' se refere ao arquivo 'views.py' dentro do aplicativo 'inicio'.
# Ela contém todas as funções de view definidas para o aplicativo.
from inicio import views

# Lista de URLs do aplicativo
# 'urlpatterns' é uma lista que contém todas as URLs mapeadas para views do
# aplicativo 'inicio'. O Django usará essa lista para determinar qual view
# chamar com base na URL solicitada pelo usuário.
urlpatterns = [
    # A função 'path' é chamada para criar um mapeamento entre uma URL e uma view.
    # Neste caso, estamos associando a URL vazia ('') à função 'index' definida
    # no arquivo 'views.py'. Isso significa que quando um usuário acessar a raiz
    # do site (a URL principal), o Django chamará a view 'index'.
    # O terceiro parâmetro, 'name='index'', atribui um nome à URL.
    # Isso facilita referenciar essa URL em outras partes do código, como em templates
    # ou redirecionamentos.
    path("", views.index, name="index"),
    path("<int:pergunta_id>/", views.detalhes, name="detalhes"),
    path("<int:pergunta_id>/resultados", views.resultados, name="resultados"),
    path("<int:pergunta_id>/votos", views.votos, name="votos"),
]

# Isso garante que, quando um usuário acessar a raiz do site (por exemplo, 'www.seusite.com/'),
# a view 'index' será chamada e o Django retornará a resposta definida nela,
# que no caso é a mensagem "Olá, mundo. Essa é minha primeira view".
