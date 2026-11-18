from django.shortcuts import render
from django.http import HttpResponse
from .models import Filme, Projeto, Categoria  # Importando com letra maiúscula (boa prática)


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

def lista_projetos(request):
    contexto = {
        'projetos': Projeto.objects.all(),
    }
    return render(request, 'projetos.html', contexto)

def lista_filmes(request):
    contexto = {
        'filmes': Filme.objects.all(),
    }
    return render(request, 'filme.html', contexto)

def listar_categoria(request):
    contexto = {
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'categoria.html', contexto)  # Padronizado para o plural