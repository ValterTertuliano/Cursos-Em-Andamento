from django.shortcuts import render

# Create your views here.


# isso é uma view para a pagina inicial
def home(request):
    contexto = {
        'title': "Pagina Inicial"
    }
    return render(
        request,
        "homeapp/home.html",
        contexto,
    )
