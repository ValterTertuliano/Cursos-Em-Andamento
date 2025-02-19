from django.shortcuts import render
from blogapp.data import posts

# Create your views here.
# isso é uma view para a rota blog
def blog(request):
    print("Essa é a view da blog - mudei para pasta blogapp - url aninhada")
    contexto = {
        'posts': posts
    }
    return render(request, "blogapp/blog.html", contexto)


def exemploblog(request):
    print("essa é uma view de uma url aninhada com blog - ")
    return render(request, "blogapp/exemplo.html")
