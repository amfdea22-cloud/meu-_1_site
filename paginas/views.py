from django.shortcuts import render

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
    projetos = {
        'projetos': ['Calculadora ', 'Sobre', 'Contato', 'Meu Site']
    }
    return render(request, 'projetos.html', projetos)
    