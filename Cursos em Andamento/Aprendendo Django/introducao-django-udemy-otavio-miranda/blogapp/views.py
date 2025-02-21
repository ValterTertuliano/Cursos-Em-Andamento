from django.shortcuts import render
from blogapp.data import posts
from django.http import Http404
# Create your views here.
# isso é uma view para a rota blog

def blog(request):
    contexto = {
        'text': "Olá usando context",
        'posts': posts,
        'title': 'Inicio do blog ',
    }
    return render(request, "blogapp/blog.html", contexto)


def exemploblog(request):
    contexto = {
        'title': 'Url aninhada',
    }
    return render(request, "blogapp/exemplo.html", contexto)

def post_view(request, id):
    print(f"{request}\nId: {id}")
    
    post_encontrado = None
    for post in posts:
        if post['id'] == id:
            post_encontrado = post
            break

    if post_encontrado is None:
        raise Http404(f"Pagina Não Existe, acompanhe o id que vai até {len(posts)}")

    context = {
        'post': post_encontrado,
        'text': f"Abrindo conteudo do post {id}",
        'title': post_encontrado['title'],
    }
    return render(request, "blogapp/post.html", context) 

# estou na aula 442 