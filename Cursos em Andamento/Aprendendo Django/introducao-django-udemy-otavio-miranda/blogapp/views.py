from django.shortcuts import render
from blogapp.data import posts

# Create your views here.
# isso é uma view para a rota blog

def blog(request):
    contexto = {
        'text': "Olá usando context",
        'posts': posts
    }
    return render(request, "blogapp/blog.html", contexto)


def exemploblog(request):
    return render(request, "blogapp/exemplo.html")

def post_view(request, id):
    print(f"{request}\nId: {id}")
    context = {
        'posts': posts
    }
    return render(request, "blogapp/blog.html", context) 