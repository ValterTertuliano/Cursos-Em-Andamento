from django.http import HttpResponse  # type: ignore
from inicio.models import Pergunta
from django.template import loader  # type: ignore


def index(request):
    lista_de_perguntas = Pergunta.objects.order_by("-data_publicacao")[:5]
    template = loader.get_template("inicio/index.html")
    context = {
        "lista_de_perguntas": lista_de_perguntas,
    }
    return HttpResponse(template.render(context, request))


def detalhes(request, pergunta_id):
    return HttpResponse("Pergunta Atual: ", pergunta_id)


def resultados(request, pergunta_id):
    return HttpResponse("O resultado da pergunta: ", pergunta_id)


def votos(request, pergunta_id):
    return HttpResponse("Você esta votando para a pergunta: ", pergunta_id)
