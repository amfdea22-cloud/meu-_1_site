from django.shortcuts import render
from django.http import HttpResponse
from .models import  filme
from .models import projeto


def inicio(request):
    contexto = {
        'nome': 'Andréa França',
        'cidade': 'Recife',
        'cursos': ['Python', 'Django', 'HTML', 'CSS'],
        'hobbies': ['Ler', 'Estudar', 'Comer']
    }
    return render(request, 'inicio.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def projetos(request):
    contexto = {
        'projetos': projeto.objects.all(),
        'filmes': filme.objects.all(),
    }
    return render(request, 'projetos.html', contexto)


    