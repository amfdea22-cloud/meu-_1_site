from django.shortcuts import render, redirect
from .models import Filme, Projeto, Categoria
from .forms import ProjetoForm, CategoriaForm


def inicio(request):
    contexto = {
        'nome': 'Andréa França',
        'cidade': 'Recife',
        'cursos': ['Python', 'Django', 'HTML', 'CSS'],
        'hobbies': ['Ler', 'Estudar', 'Comer'],
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
    return render(request, 'categoria.html', contexto)


def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projetos")
    else:
        form = ProjetoForm()
    return render(request, "novo_projeto.html", {"form": form})


def nova_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categoria")
    else:
        form = CategoriaForm()
    return render(request, "nova_categoria.html", {"form": form})