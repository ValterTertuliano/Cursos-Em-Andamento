# Importação do módulo HttpResponse do Django
# O HttpResponse é utilizado para retornar uma resposta HTTP
# ao navegador, com o conteúdo que será exibido ao usuário.
# Neste caso, estamos retornando uma simples mensagem de
# texto.
from django.http import HttpResponse

# Criamos a função 'index', que será a nossa view.
# Uma 'view' no Django é responsável por receber a requisição
# HTTP do usuário, processá-la e retornar uma resposta.
# A função 'index' será chamada quando um usuário acessar a
# URL correspondente a ela, definida no arquivo de URLs.
# O parâmetro 'request' é o objeto que contém todas as
# informações da requisição HTTP feita pelo usuário, como
# dados de formulário, cabeçalhos, cookies, entre outros.

# É importante lembrar que, para que essa view funcione, ela
# precisa ser mapeada para uma URL específica dentro do
# Django. O mapeamento de URLs no Django é feito dentro do
# arquivo 'urls.py'.

# Agora, você precisará criar um arquivo 'urls.py' dentro da
# pasta do seu aplicativo (neste caso, o aplicativo se chama
# 'inicio').
# Dentro desse arquivo, você irá associar uma URL à view
# 'index'.
# Exemplo de como isso seria feito no arquivo 'urls.py'
# dentro de 'inicio':

# from django.urls import path
# from . import views  # importando a função 'index' do arquivo 'views.py'

# urlpatterns = [
#     path('', views.index, name='index'),  # A URL vazia ('') será mapeada

#     # para a view 'index'. Quando um usuário acessar o site na raiz,

#     # o Django chamará a função 'index' e exibirá a mensagem "Olá, mundo".
# ]


# Ao fazer isso, sempre que um usuário acessar a URL mapeada (no caso, a raiz do site),
# o Django chamará a função 'index' e exibirá a mensagem abaixo.
def index(request):
    return HttpResponse(
        "Olá, mundo. Essa é minha primeira view"
    )  # Retorna a resposta "Olá, mundo"
