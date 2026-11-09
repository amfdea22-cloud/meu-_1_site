from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    dados = {
        'nome': 'Andréa França',
        'idade': 40,
        'altura': 1.60,
        'pets': ['Cachorro', 'Gato', 'Pássaro']
    }
    return render(request, 'inicio.html',dados)

def sobre(request):
    return HttpResponse(
        "<h1>Sobre mim</h1>"
        "<p>Meu nome é Andréa França e estou aprendendo a usar o Django.</p>"
        "<br><a href='/'>Início</a> | <a href='/contato/'>Contato</a>"
    )

def contato(request):
    return HttpResponse(
        "<h1>Contato</h1>"
        "<p>Entre em contato comigo pelo e-mail: amfdea22@gmail.com</p>"
        "<br><a href='/'>Início</a> | "
        " <a href='/sobre/'>Sobre</a>"
    )
    